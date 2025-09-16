import pytest
import json
from unittest.mock import Mock, patch
from canvas_openapi.builder import OpenAPIBuilder
from parse_canvas_markdown import Resource, Endpoint, Parameter


class TestOpenAPIBuilder:
    
    def test_init_creates_valid_base_spec(self, openapi_builder):
        spec = openapi_builder.get_spec()
        
        assert spec["openapi"] == "3.1.0"
        assert spec["info"]["title"] == "Canvas LMS API"
        assert spec["info"]["version"] == "1.0.0"
        assert "servers" in spec
        assert "security" in spec
        assert "components" in spec
        assert "paths" in spec
        assert spec["paths"] == {}
        assert spec["components"]["schemas"] == {}
        
    def test_normalize_path_adds_leading_slash(self, openapi_builder):
        result = openapi_builder._normalize_path("api/v1/users")
        assert result == "/api/v1/users"
        
    def test_normalize_path_preserves_existing_slash(self, openapi_builder):
        result = openapi_builder._normalize_path("/api/v1/users")
        assert result == "/api/v1/users"
        
    def test_normalize_path_converts_colon_params_to_braces(self, openapi_builder):
        result = openapi_builder._normalize_path("/api/v1/users/:id")
        assert result == "/api/v1/users/{id}"
        
    def test_normalize_path_handles_multiple_params(self, openapi_builder):
        result = openapi_builder._normalize_path("/api/v1/courses/:course_id/users/:user_id")
        assert result == "/api/v1/courses/{course_id}/users/{user_id}"
        
    def test_normalize_path_strips_whitespace(self, openapi_builder):
        result = openapi_builder._normalize_path("  /api/v1/users  ")
        assert result == "/api/v1/users"
        
    def test_generate_operation_id_get_with_id_param(self, openapi_builder):
        result = openapi_builder._generate_operation_id("get", "/users/{id}", "Users")
        assert result == "get_users"
        
    def test_generate_operation_id_get_list(self, openapi_builder):
        result = openapi_builder._generate_operation_id("get", "/users", "Users")
        assert result == "list_users"
        
    def test_generate_operation_id_post(self, openapi_builder):
        result = openapi_builder._generate_operation_id("post", "/users", "Users")
        assert result == "create_users"
        
    def test_generate_operation_id_put(self, openapi_builder):
        result = openapi_builder._generate_operation_id("put", "/users/{id}", "Users")
        assert result == "update_users"
        
    def test_generate_operation_id_patch(self, openapi_builder):
        result = openapi_builder._generate_operation_id("patch", "/users/{id}", "Users")
        assert result == "update_users"
        
    def test_generate_operation_id_delete(self, openapi_builder):
        result = openapi_builder._generate_operation_id("delete", "/users/{id}", "Users")
        assert result == "delete_users"
        
    def test_generate_operation_id_complex_path(self, openapi_builder):
        result = openapi_builder._generate_operation_id("get", "/courses/{course_id}/assignments", "Assignments")
        assert result == "get_assignments"
        
    def test_get_parameter_schema_string_default(self, openapi_builder):
        param = Parameter(name="test", type=None, description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "string"}
        
    def test_get_parameter_schema_integer(self, openapi_builder):
        param = Parameter(name="test", type="integer", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "integer"}
        
    def test_get_parameter_schema_int(self, openapi_builder):
        param = Parameter(name="test", type="int", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "integer"}
        
    def test_get_parameter_schema_number(self, openapi_builder):
        param = Parameter(name="test", type="number", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "number"}
        
    def test_get_parameter_schema_float(self, openapi_builder):
        param = Parameter(name="test", type="float", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "number"}
        
    def test_get_parameter_schema_boolean(self, openapi_builder):
        param = Parameter(name="test", type="boolean", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "boolean"}
        
    def test_get_parameter_schema_bool(self, openapi_builder):
        param = Parameter(name="test", type="bool", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "boolean"}
        
    def test_get_parameter_schema_array(self, openapi_builder):
        param = Parameter(name="test", type="array", description="", required=False, location="query")
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "array", "items": {"type": "string"}}
        
    def test_get_parameter_schema_with_enum(self, openapi_builder):
        param = Parameter(
            name="test", 
            type="string", 
            description="", 
            required=False, 
            location="query",
            enum_values=["option1", "option2", "option3"]
        )
        schema = openapi_builder._get_parameter_schema(param)
        assert schema == {"type": "string", "enum": ["option1", "option2", "option3"]}
        
    def test_build_parameters_path_query_header(self, openapi_builder):
        parameters = [
            Parameter(name="id", type="integer", description="User ID", required=True, location="path"),
            Parameter(name="include", type="array", description="Include fields", required=False, location="query"),
            Parameter(name="authorization", type="string", description="Auth header", required=True, location="header")
        ]
        
        result = openapi_builder._build_parameters(parameters)
        
        assert len(result) == 3
        
        path_param = next(p for p in result if p["in"] == "path")
        assert path_param["name"] == "id"
        assert path_param["required"] is True
        assert path_param["schema"]["type"] == "integer"
        
        query_param = next(p for p in result if p["in"] == "query")
        assert query_param["name"] == "include"
        assert query_param["required"] is False
        assert query_param["schema"]["type"] == "array"
        
        header_param = next(p for p in result if p["in"] == "header")
        assert header_param["name"] == "authorization"
        assert header_param["required"] is True
        
    def test_build_parameters_excludes_body_form_params(self, openapi_builder):
        parameters = [
            Parameter(name="id", type="integer", description="User ID", required=True, location="path"),
            Parameter(name="name", type="string", description="User name", required=True, location="body"),
            Parameter(name="email", type="string", description="User email", required=True, location="form")
        ]
        
        result = openapi_builder._build_parameters(parameters)
        
        assert len(result) == 1
        assert result[0]["name"] == "id"
        
    def test_build_request_body_with_form_params(self, openapi_builder):
        body_params = [
            Parameter(name="name", type="string", description="User name", required=True, location="form"),
            Parameter(name="email", type="string", description="User email", required=False, location="form")
        ]
        
        result = openapi_builder._build_request_body(body_params)
        
        assert result["required"] is True
        assert "application/json" in result["content"]
        assert "application/x-www-form-urlencoded" in result["content"]
        
        schema = result["content"]["application/json"]["schema"]
        assert schema["type"] == "object"
        assert "name" in schema["properties"]
        assert "email" in schema["properties"]
        assert schema["required"] == ["name"]
        
    def test_build_request_body_with_body_params(self, openapi_builder):
        body_params = [
            Parameter(name="user_data", type="object", description="User data", required=True, location="body")
        ]
        
        result = openapi_builder._build_request_body(body_params)
        
        assert result["required"] is True
        schema = result["content"]["application/json"]["schema"]
        assert "user_data" in schema["properties"]
        
    def test_build_responses_default(self, openapi_builder):
        endpoint = Endpoint(
            name="Test",
            method="GET",
            path="/test",
            description="Test endpoint"
        )
        
        result = openapi_builder._build_responses(endpoint)
        
        assert "200" in result
        assert result["200"]["description"] == "Successful response"
        assert "400" in result
        assert "401" in result
        assert "403" in result
        assert "404" in result
        assert "500" in result
        
    def test_build_responses_with_schema(self, openapi_builder):
        endpoint = Endpoint(
            name="Test",
            method="GET",
            path="/test",
            description="Test endpoint",
            response_schema={"type": "object", "properties": {"id": {"type": "integer"}}}
        )
        
        result = openapi_builder._build_responses(endpoint)
        
        assert "content" in result["200"]
        assert "application/json" in result["200"]["content"]
        schema = result["200"]["content"]["application/json"]["schema"]
        assert schema["type"] == "object"
        
    def test_process_response_schema_empty(self, openapi_builder):
        result = openapi_builder._process_response_schema({})
        assert result == {"type": "object"}
        
    def test_process_response_schema_none(self, openapi_builder):
        result = openapi_builder._process_response_schema(None)
        assert result == {"type": "object"}
        
    def test_process_response_schema_with_type(self, openapi_builder):
        schema = {"type": "array", "items": {"type": "string"}}
        result = openapi_builder._process_response_schema(schema)
        assert result == schema
        
    def test_process_response_schema_without_type(self, openapi_builder):
        schema = {"properties": {"id": {"type": "integer"}}}
        result = openapi_builder._process_response_schema(schema)
        assert result == {"type": "object", "additionalProperties": True}
        
    def test_add_endpoint_basic(self, openapi_builder, sample_endpoint, sample_resource):
        openapi_builder._add_endpoint(sample_endpoint, sample_resource)
        
        spec = openapi_builder.get_spec()
        assert "/api/v1/users/{id}" in spec["paths"]
        
        operation = spec["paths"]["/api/v1/users/{id}"]["get"]
        assert operation["summary"] == "Get User"
        assert operation["operationId"] == "get_users"
        assert operation["tags"] == ["Users"]
        assert "security" in operation
        
    def test_add_endpoint_with_scope(self, openapi_builder, sample_resource):
        endpoint = Endpoint(
            name="Test Endpoint",
            method="POST",
            path="/api/v1/test",
            description="Test description",
            scope="url:POST|/api/v1/test"
        )
        
        openapi_builder._add_endpoint(endpoint, sample_resource)
        
        spec = openapi_builder.get_spec()
        operation = spec["paths"]["/api/v1/test"]["post"]
        assert "Required OAuth scope: url:POST|/api/v1/test" in operation["description"]
        
    def test_add_endpoint_with_parameters(self, openapi_builder, sample_resource):
        endpoint = Endpoint(
            name="Test Endpoint",
            method="GET",
            path="/api/v1/test/:id",
            description="Test description",
            parameters=[
                Parameter(name="id", type="integer", description="ID", required=True, location="path"),
                Parameter(name="filter", type="string", description="Filter", required=False, location="query")
            ]
        )
        
        openapi_builder._add_endpoint(endpoint, sample_resource)
        
        spec = openapi_builder.get_spec()
        operation = spec["paths"]["/api/v1/test/{id}"]["get"]
        assert "parameters" in operation
        assert len(operation["parameters"]) == 2
        
    def test_add_endpoint_post_with_body_params(self, openapi_builder, sample_resource):
        endpoint = Endpoint(
            name="Create Test",
            method="POST",
            path="/api/v1/test",
            description="Create test",
            parameters=[
                Parameter(name="name", type="string", description="Name", required=True, location="form"),
                Parameter(name="description", type="string", description="Description", required=False, location="form")
            ]
        )
        
        openapi_builder._add_endpoint(endpoint, sample_resource)
        
        spec = openapi_builder.get_spec()
        operation = spec["paths"]["/api/v1/test"]["post"]
        assert "requestBody" in operation
        
    def test_add_resource(self, openapi_builder, sample_resource):
        openapi_builder.add_resource(sample_resource)
        
        spec = openapi_builder.get_spec()
        assert len(spec["paths"]) == 1
        assert "/api/v1/users/{id}" in spec["paths"]
        
    def test_add_schemas(self, openapi_builder):
        schemas = {
            "User": {"type": "object", "properties": {"id": {"type": "integer"}}},
            "Course": {"type": "object", "properties": {"name": {"type": "string"}}}
        }
        
        openapi_builder.add_schemas(schemas)
        
        spec = openapi_builder.get_spec()
        assert "User" in spec["components"]["schemas"]
        assert "Course" in spec["components"]["schemas"]
        assert spec["components"]["schemas"]["User"]["type"] == "object"
        
    def test_add_schemas_prevents_duplicates(self, openapi_builder):
        schemas = {"User": {"type": "object", "properties": {"id": {"type": "integer"}}}}
        
        openapi_builder.add_schemas(schemas)
        openapi_builder.add_schemas(schemas)
        
        spec = openapi_builder.get_spec()
        assert len(spec["components"]["schemas"]) == 1
        
    def test_to_json(self, openapi_builder):
        result = openapi_builder.to_json()
        
        parsed = json.loads(result)
        assert parsed["openapi"] == "3.1.0"
        assert parsed["info"]["title"] == "Canvas LMS API"
        
    def test_to_yaml_produces_valid_yaml(self, openapi_builder):
        result = openapi_builder.to_yaml()
        
        assert isinstance(result, str)
        assert "openapi:" in result or "openapi: " in result
        assert "Canvas LMS API" in result
        assert "paths:" in result or "paths: " in result
        
    def test_to_yaml_contains_expected_structure(self, openapi_builder, sample_resource):
        openapi_builder.add_resource(sample_resource)
        result = openapi_builder.to_yaml()
        
        assert isinstance(result, str)
        assert len(result) > 0
        assert "openapi:" in result or "openapi: " in result
        assert "info:" in result or "info: " in result
        assert "paths:" in result or "paths: " in result
