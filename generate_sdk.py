#!/usr/bin/env python3

import argparse
import subprocess
import sys
import shutil
from pathlib import Path
from canvas_openapi.generator import CanvasOpenAPIGenerator


def run_command(cmd: list, cwd: Path = None) -> bool:
    try:
        print(f"🔧 Running: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate Python SDK from Canvas API OpenAPI specification"
    )
    parser.add_argument(
        "--docs-dir",
        default="data/canvas_api_resources",
        help="Directory containing Canvas API markdown files (default: data/canvas_api_resources)"
    )
    parser.add_argument(
        "--output-dir",
        default="sdk",
        help="Output directory for generated SDK (default: sdk)"
    )
    parser.add_argument(
        "--package-name",
        default="canvas_sdk",
        help="Name for the generated Python package (default: canvas_sdk)"
    )
    parser.add_argument(
        "--regenerate-spec",
        action="store_true",
        help="Regenerate OpenAPI spec before generating SDK"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean output directory before generating"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    try:
        output_path = Path(args.output_dir)
        spec_file = Path("output/canvas_api.openapi.json")
        
        if args.clean and output_path.exists():
            print(f"🧹 Cleaning output directory: {output_path}")
            shutil.rmtree(output_path)
        
        if args.regenerate_spec or not spec_file.exists():
            print("📋 Generating OpenAPI specification...")
            generator = CanvasOpenAPIGenerator(docs_dir=args.docs_dir)
            saved_files = generator.save_spec(formats=["json"])
            spec_file = Path(saved_files["json"])
        
        if not spec_file.exists():
            print(f"❌ OpenAPI spec file not found: {spec_file}")
            print("💡 Run with --regenerate-spec to generate it first")
            sys.exit(1)
        
        print(f"🚀 Generating Python SDK from OpenAPI spec...")
        print(f"📄 Spec file: {spec_file}")
        print(f"📁 Output: {output_path}")
        print(f"📦 Package: {args.package_name}")
        print()
        
        if not shutil.which("openapi-python-client"):
            print("📦 Installing openapi-python-client...")
            if not run_command([sys.executable, "-m", "pip", "install", "openapi-python-client"]):
                sys.exit(1)
        
        cmd = [
            "openapi-python-client",
            "generate",
            "--path", str(spec_file),
            "--output-path", str(output_path),
            "--overwrite"
        ]
        
        if not run_command(cmd):
            sys.exit(1)
        
        print(f"\n🎉 Successfully generated Canvas LMS Python SDK!")
        print(f"📁 Location: {output_path}")
        
        readme_path = output_path / "README.md"
        if readme_path.exists():
            print(f"📖 Documentation: {readme_path}")
        
        print(f"\n💡 Quick start:")
        print(f"   1. Install: pip install -e {output_path}")
        print(f"   2. Import: from {args.package_name} import Client")
        print(f"   3. Use: client = Client(base_url='https://your-canvas.com/api/v1', token='your-token')")
        
        pyproject_path = output_path / "pyproject.toml"
        if pyproject_path.exists():
            print(f"\n🔧 Development:")
            print(f"   cd {output_path}")
            print(f"   pip install -e .")
            print(f"   python -c \"from {args.package_name} import Client; print('SDK imported successfully!')\"")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
