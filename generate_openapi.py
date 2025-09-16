#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
from canvas_openapi.generator import CanvasOpenAPIGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Generate OpenAPI specification from Canvas API documentation"
    )
    parser.add_argument(
        "--docs-dir",
        default="data/canvas_api_resources",
        help="Directory containing Canvas API markdown files (default: data/canvas_api_resources)"
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory for generated files (default: output)"
    )
    parser.add_argument(
        "--format",
        choices=["json", "yaml", "both"],
        default="both",
        help="Output format (default: both)"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate the generated OpenAPI specification"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    try:
        generator = CanvasOpenAPIGenerator(docs_dir=args.docs_dir)
        
        formats = []
        if args.format in ["json", "both"]:
            formats.append("json")
        if args.format in ["yaml", "both"]:
            formats.append("yaml")
        
        print("🚀 Starting Canvas API OpenAPI generation...")
        print(f"📂 Source: {args.docs_dir}")
        print(f"📁 Output: {args.output_dir}")
        print(f"📄 Format: {', '.join(formats)}")
        print()
        
        saved_files = generator.save_spec(
            output_dir=args.output_dir,
            formats=formats
        )
        
        if args.validate:
            print("\n🔍 Validating OpenAPI specification...")
            if not generator.validate_spec():
                sys.exit(1)
        
        print(f"\n🎉 Successfully generated OpenAPI specification!")
        for format_type, file_path in saved_files.items():
            print(f"   📄 {format_type.upper()}: {file_path}")
        
        print(f"\n💡 Next steps:")
        print(f"   1. Generate Python SDK: python generate_sdk.py")
        print(f"   2. View spec online: https://editor.swagger.io/ (paste the JSON/YAML)")
        print(f"   3. Generate other clients: https://openapi-generator.tech/")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
