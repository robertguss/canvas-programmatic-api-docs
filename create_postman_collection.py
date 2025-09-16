import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
from parse_canvas_markdown import parse_all_resources, Resource, Endpoint, Parameter


class PostmanCollectionGenerator:
    def __init__(self, base_url="{{base_url}}", access_token="{{access_token}}", uuid_fn=None):
        self.collection_id = str((uuid_fn or uuid.uuid4)())
        self.base_url = base_url
        self.access_token = access_token
    
    def generate_collection(self, resources: Dict[str, Resource]) -> Dict[str, Any]:
        collection = {
            "info": {
                "name": "Canvas API (Generated from Markdown)",
                "description": f"Canvas LMS API collection generated from markdown documentation on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
                "_postman_id": self.collection_id
            },
            "auth": {
                "type": "bearer",
                "bearer": [
                    {
                        "key": "token",
                        "value": self.access_token,
                        "type": "string"
                    }
                ]
            },
            "variable": [
                {
                    "key": "base_url",
                    "value": "https://canvas.instructure.com",
                    "type": "string"
                },
                {
                    "key": "access_token",
                    "value": "your_canvas_access_token_here",
                    "type": "string"
                }
            ],
            "item": []
        }
        
        # Sort resources by name for consistent ordering
        sorted_resources = sorted(resources.items(), key=lambda x: x[1].name)
        
        for resource_key, resource in sorted_resources:
            folder = self._create_resource_folder(resource)
            collection["item"].append(folder)
        
        return collection
    
    def _create_resource_folder(self, resource: Resource) -> Dict[str, Any]:
        folder = {
            "name": resource.name,
            "description": resource.description,
            "item": []
        }
        
        # Sort endpoints by method and path
        sorted_endpoints = sorted(resource.endpoints, key=lambda x: (x.method, x.path))
        
        for endpoint in sorted_endpoints:
            request_item = self._create_request_item(endpoint)
            folder["item"].append(request_item)
        
        return folder
    
    def _create_request_item(self, endpoint: Endpoint) -> Dict[str, Any]:
        # Convert Canvas path format to Postman format
        postman_path = self._convert_path_to_postman(endpoint.path)
        
        # Build URL object
        url_obj = self._build_url_object(postman_path, endpoint.parameters)
        
        # Build request body if needed
        body = self._build_request_body(endpoint)
        
        # Create description with scope info
        description = endpoint.description
        if endpoint.scope:
            description += f"\n\n**OAuth Scope:** `{endpoint.scope}`"
        
        request_item = {
            "name": endpoint.name,
            "request": {
                "method": endpoint.method,
                "header": [],
                "url": url_obj,
                "description": description
            }
        }
        
        # Add body for POST/PUT/PATCH requests
        if body:
            request_item["request"]["body"] = body
        
        return request_item
    
    def _convert_path_to_postman(self, canvas_path: str) -> str:
        # Convert Canvas :param format to Postman :param format
        # Canvas uses :course_id, Postman uses :course_id (same format)
        return canvas_path
    
    def _build_url_object(self, path: str, parameters: List[Parameter]) -> Dict[str, Any]:
        # Split path into segments
        path_segments = [seg for seg in path.split('/') if seg]
        
        # Build raw URL
        raw_url = f"{self.base_url}{path}"
        
        # Extract path variables
        path_variables = []
        query_params = []
        
        for param in parameters:
            if param.location == 'path':
                path_variables.append({
                    "key": param.name,
                    "value": f"<{param.name}>",
                    "description": param.description
                })
            elif param.location == 'query':
                query_params.append({
                    "key": param.name,
                    "value": "",
                    "description": param.description,
                    "disabled": not param.required
                })
        
        url_obj = {
            "raw": raw_url,
            "host": ["{{base_url}}"],
            "path": path_segments
        }
        
        if path_variables:
            url_obj["variable"] = path_variables
        
        if query_params:
            url_obj["query"] = query_params
        
        return url_obj
    
    def _build_request_body(self, endpoint: Endpoint) -> Dict[str, Any]:
        body_params = [p for p in endpoint.parameters if p.location == 'body']
        
        if not body_params or endpoint.method == 'GET':
            return None
        
        # Create form-data body for most Canvas API endpoints
        formdata = []
        for param in body_params:
            formdata.append({
                "key": param.name,
                "value": "",
                "description": param.description,
                "type": "text",
                "disabled": not param.required
            })
        
        return {
            "mode": "formdata",
            "formdata": formdata
        }
    
    def save_collection(self, collection: Dict[str, Any], output_path: Path):
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(collection, f, indent=2, ensure_ascii=False)


def main():
    # Parse all markdown resources
    resources_dir = Path("data/canvas_api_resources")
    if not resources_dir.exists():
        print(f"Error: Resources directory not found: {resources_dir}")
        return
    
    print("Parsing Canvas API markdown documentation...")
    resources = parse_all_resources(resources_dir)
    
    if not resources:
        print("No resources found to parse!")
        return
    
    print(f"Found {len(resources)} resources with endpoints:")
    total_endpoints = 0
    for name, resource in resources.items():
        endpoint_count = len(resource.endpoints)
        total_endpoints += endpoint_count
        print(f"  {resource.name}: {endpoint_count} endpoints")
    
    print(f"\nTotal endpoints: {total_endpoints}")
    
    # Generate Postman collection
    print("\nGenerating Postman collection...")
    generator = PostmanCollectionGenerator()
    collection = generator.generate_collection(resources)
    
    # Save to output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "canvas_api.postman_collection.json"
    
    generator.save_collection(collection, output_path)
    
    print(f"✅ Postman collection saved to: {output_path}")
    print(f"📊 Collection contains {len(collection['item'])} resource folders")
    print("\n🚀 Ready to import into Postman!")
    print("\n📝 Don't forget to:")
    print("   1. Set your Canvas base URL in the 'base_url' variable")
    print("   2. Set your Canvas access token in the 'access_token' variable")


if __name__ == "__main__":
    main()
