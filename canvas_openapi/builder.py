from typing import Dict, Any, List, Optional
import re
from dataclasses import asdict
from parse_canvas_markdown import Resource, Endpoint, Parameter


class OpenAPIBuilder:
    def __init__(self):
        self.spec = {
            "openapi": "3.1.0",
            "info": {
                "title": "Canvas LMS API",
                "description": "The Canvas LMS REST API provides a way to access and modify data externally from the main application, in JSON format.",
                "version": "1.0.0",
                "contact": {
                    "name": "Canvas LMS API Documentation",
                    "url": "https://canvas.instructure.com/doc/api/"
                }
            },
            "servers": [
                {
                    "url": "https://{canvas_domain}/api/v1",
                    "description": "Canvas LMS API Server",
                    "variables": {
                        "canvas_domain": {
                            "default": "canvas.instructure.com",
                            "description": "Your Canvas domain (e.g., myschool.instructure.com)"
                        }
                    }
                }
            ],
            "security": [
                {"bearerAuth": []}
            ],
            "components": {
                "securitySchemes": {
                    "bearerAuth": {
                        "type": "http",
                        "scheme": "bearer",
                        "description": "Canvas API access token"
                    }
                },
                "schemas": {}
            },
            "paths": {}
        }
        self.schemas_added = set()

    def add_resource(self, resource: Resource):
        for endpoint in resource.endpoints:
            self._add_endpoint(endpoint, resource)

    def _add_endpoint(self, endpoint: Endpoint, resource: Resource):
        path = self._normalize_path(endpoint.path)
        method = endpoint.method.lower()
        
        if path not in self.spec["paths"]:
            self.spec["paths"][path] = {}
        
        operation = {
            "summary": endpoint.name or f"{method.upper()} {path}",
            "description": endpoint.description or endpoint.name or "",
            "operationId": self._generate_operation_id(method, path, resource.name),
            "tags": [resource.name],
            "security": [{"bearerAuth": []}]
        }

        if endpoint.scope:
            operation["description"] += f"\n\nRequired OAuth scope: {endpoint.scope}"

        if endpoint.parameters:
            operation["parameters"] = self._build_parameters(endpoint.parameters)

        if method in ["post", "put", "patch"] and endpoint.parameters:
            body_params = [p for p in endpoint.parameters if p.location in ["form", "body"]]
            if body_params:
                operation["requestBody"] = self._build_request_body(body_params)

        operation["responses"] = self._build_responses(endpoint)

        self.spec["paths"][path][method] = operation

    def _normalize_path(self, path: str) -> str:
        path = path.strip()
        if not path.startswith('/'):
            path = '/' + path
        
        path = re.sub(r':(\w+)', r'{\1}', path)
        
        return path

    def _generate_operation_id(self, method: str, path: str, resource_name: str) -> str:
        path_parts = [p for p in path.split('/') if p and not p.startswith('{')]
        
        if method == "get":
            if path.endswith('}') or 'id' in path.lower():
                action = "get"
            else:
                action = "list"
        elif method == "post":
            action = "create"
        elif method == "put":
            action = "update"
        elif method == "patch":
            action = "update"
        elif method == "delete":
            action = "delete"
        else:
            action = method

        if path_parts:
            resource_part = path_parts[-1] if len(path_parts) > 1 else resource_name.lower()
        else:
            resource_part = resource_name.lower()

        return f"{action}_{resource_part}"

    def _build_parameters(self, parameters: List[Parameter]) -> List[Dict[str, Any]]:
        openapi_params = []
        
        for param in parameters:
            if param.location in ["path", "query", "header"]:
                param_spec = {
                    "name": param.name,
                    "in": param.location,
                    "required": param.required,
                    "description": param.description or "",
                    "schema": self._get_parameter_schema(param)
                }
                openapi_params.append(param_spec)
        
        return openapi_params

    def _get_parameter_schema(self, param: Parameter) -> Dict[str, Any]:
        schema = {"type": "string"}
        
        if param.type:
            param_type = param.type.lower()
            if param_type in ["integer", "int"]:
                schema["type"] = "integer"
            elif param_type in ["number", "float", "double"]:
                schema["type"] = "number"
            elif param_type in ["boolean", "bool"]:
                schema["type"] = "boolean"
            elif param_type == "array":
                schema = {
                    "type": "array",
                    "items": {"type": "string"}
                }
        
        if param.enum_values:
            schema["enum"] = param.enum_values
        
        return schema

    def _build_request_body(self, body_params: List[Parameter]) -> Dict[str, Any]:
        properties = {}
        required = []
        
        for param in body_params:
            properties[param.name] = {
                "type": "string",
                "description": param.description or ""
            }
            if param.required:
                required.append(param.name)
        
        schema = {
            "type": "object",
            "properties": properties
        }
        
        if required:
            schema["required"] = required
        
        return {
            "required": True,
            "content": {
                "application/json": {
                    "schema": schema
                },
                "application/x-www-form-urlencoded": {
                    "schema": schema
                }
            }
        }

    def _build_responses(self, endpoint: Endpoint) -> Dict[str, Any]:
        responses = {
            "200": {
                "description": "Successful response"
            }
        }
        
        if endpoint.response_schema:
            responses["200"]["content"] = {
                "application/json": {
                    "schema": self._process_response_schema(endpoint.response_schema)
                }
            }
        
        responses.update({
            "400": {"description": "Bad Request"},
            "401": {"description": "Unauthorized"},
            "403": {"description": "Forbidden"},
            "404": {"description": "Not Found"},
            "500": {"description": "Internal Server Error"}
        })
        
        return responses

    def _process_response_schema(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        if not schema:
            return {"type": "object"}
        
        if "type" in schema:
            return schema
        
        return {
            "type": "object",
            "additionalProperties": True
        }

    def add_schemas(self, schemas: Dict[str, Dict[str, Any]]):
        for name, schema in schemas.items():
            if name not in self.schemas_added:
                self.spec["components"]["schemas"][name] = schema
                self.schemas_added.add(name)

    def get_spec(self) -> Dict[str, Any]:
        return self.spec

    def to_yaml(self) -> str:
        try:
            from ruamel.yaml import YAML
            from io import StringIO
            
            yaml = YAML()
            yaml.preserve_quotes = True
            yaml.width = 4096
            
            stream = StringIO()
            yaml.dump(self.spec, stream)
            return stream.getvalue()
        except ImportError:
            import yaml
            return yaml.dump(self.spec, default_flow_style=False, sort_keys=False)

    def to_json(self) -> str:
        import json
        return json.dumps(self.spec, indent=2)
