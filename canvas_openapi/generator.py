import os
import json
from pathlib import Path
from typing import Dict, Any, List
from parse_canvas_markdown import CanvasMarkdownParser
from .builder import OpenAPIBuilder


class CanvasOpenAPIGenerator:
    def __init__(self, docs_dir: str = "data/canvas_api_resources"):
        self.docs_dir = Path(docs_dir)
        self.parser = CanvasMarkdownParser()
        self.builder = OpenAPIBuilder()

    def generate_spec(self) -> Dict[str, Any]:
        print("🔍 Scanning Canvas API documentation...")
        
        if not self.docs_dir.exists():
            raise FileNotFoundError(f"Documentation directory not found: {self.docs_dir}")
        
        markdown_files = list(self.docs_dir.glob("*.md"))
        if not markdown_files:
            raise FileNotFoundError(f"No markdown files found in {self.docs_dir}")
        
        print(f"📚 Found {len(markdown_files)} API documentation files")
        
        all_schemas = {}
        processed_count = 0
        
        for md_file in markdown_files:
            try:
                print(f"📖 Processing {md_file.name}...")
                resource = self.parser.parse_file(md_file)
                
                if resource and resource.endpoints:
                    self.builder.add_resource(resource)
                    processed_count += 1
                    
                    if resource.schemas:
                        all_schemas.update(resource.schemas)
                        print(f"   ✅ Added {len(resource.endpoints)} endpoints and {len(resource.schemas)} schemas")
                    else:
                        print(f"   ✅ Added {len(resource.endpoints)} endpoints")
                else:
                    print(f"   ⚠️  No endpoints found in {md_file.name}")
                    
            except Exception as e:
                print(f"   ❌ Error processing {md_file.name}: {e}")
                continue
        
        if all_schemas:
            print(f"🔧 Adding {len(all_schemas)} schemas to OpenAPI spec...")
            self.builder.add_schemas(all_schemas)
        
        spec = self.builder.get_spec()
        
        print(f"✅ Generated OpenAPI spec with:")
        print(f"   📍 {len(spec['paths'])} API paths")
        print(f"   🏷️  {len(spec['components']['schemas'])} schemas")
        print(f"   📁 {processed_count} resources processed")
        
        return spec

    def save_spec(self, output_dir: str = "output", formats: List[str] = None) -> Dict[str, str]:
        if formats is None:
            formats = ["json", "yaml"]
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        spec = self.generate_spec()
        saved_files = {}
        
        if "json" in formats:
            json_file = output_path / "canvas_api.openapi.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(spec, f, indent=2, ensure_ascii=False)
            saved_files["json"] = str(json_file)
            print(f"💾 Saved OpenAPI JSON: {json_file}")
        
        if "yaml" in formats:
            yaml_file = output_path / "canvas_api.openapi.yaml"
            with open(yaml_file, 'w', encoding='utf-8') as f:
                f.write(self.builder.to_yaml())
            saved_files["yaml"] = str(yaml_file)
            print(f"💾 Saved OpenAPI YAML: {yaml_file}")
        
        return saved_files

    def validate_spec(self) -> bool:
        try:
            from openapi_schema_pydantic import OpenAPI
            spec = self.generate_spec()
            OpenAPI.model_validate(spec)
            print("✅ OpenAPI specification is valid!")
            return True
        except ImportError:
            print("⚠️  openapi-schema-pydantic not available, skipping validation")
            return True
        except Exception as e:
            print(f"❌ OpenAPI specification validation failed: {e}")
            return False
