import pytest
import json
from pathlib import Path
from unittest.mock import patch, Mock
from canvas_openapi.generator import CanvasOpenAPIGenerator
from canvas_openapi.builder import OpenAPIBuilder


class TestOpenAPIIntegration:
    
    def test_full_workflow_minimal_resource(self, minimal_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        output_dir = tmp_path / "output"
        
        (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        spec = generator.generate_spec()
        
        assert spec["openapi"] == "3.1.0"
        assert spec["info"]["title"] == "Canvas LMS API"
        assert len(spec["paths"]) > 0
        
        saved_files = generator.save_spec(output_dir=str(output_dir))
        
        assert "json" in saved_files
        assert "yaml" in saved_files
        
        json_file = Path(saved_files["json"])
        yaml_file = Path(saved_files["yaml"])
        
        assert json_file.exists()
        assert yaml_file.exists()
        
        with open(json_file, 'r') as f:
            saved_spec = json.load(f)
            
        assert saved_spec == spec
        
        yaml_content = yaml_file.read_text()
        assert "openapi:" in yaml_content
        assert "Canvas LMS API" in yaml_content
        
    def test_full_workflow_complex_resource(self, complex_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        output_dir = tmp_path / "output"
        
        (docs_dir / "assignments.md").write_text(complex_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        spec = generator.generate_spec()
        
        assert len(spec["paths"]) >= 2
        
        paths = list(spec["paths"].keys())
        assert any("/assignments" in path for path in paths)
        
        get_assignments_path = next(path for path in paths if "/assignments" in path and not path.endswith("}"))
        get_operation = spec["paths"][get_assignments_path]["get"]
        
        assert "parameters" in get_operation
        assert len(get_operation["parameters"]) > 5
        
        param_names = [p["name"] for p in get_operation["parameters"]]
        assert "include[]" in param_names
        assert "search_term" in param_names
        assert "bucket" in param_names
        
        saved_files = generator.save_spec(output_dir=str(output_dir), formats=["json"])
        
        json_file = Path(saved_files["json"])
        assert json_file.exists()
        
        with open(json_file, 'r') as f:
            saved_spec = json.load(f)
            
        assert saved_spec["paths"] == spec["paths"]
        
    def test_full_workflow_multiple_resources(self, minimal_resource_file, complex_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        output_dir = tmp_path / "output"
        
        (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
        (docs_dir / "assignments.md").write_text(complex_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        spec = generator.generate_spec()
        
        assert len(spec["paths"]) >= 4
        
        paths = list(spec["paths"].keys())
        user_paths = [path for path in paths if "/users" in path]
        assignment_paths = [path for path in paths if "/assignments" in path]
        
        assert len(user_paths) >= 2
        assert len(assignment_paths) >= 2
        
        tags = set()
        for path_data in spec["paths"].values():
            for operation in path_data.values():
                if "tags" in operation:
                    tags.update(operation["tags"])
                    
        assert "Users API" in tags
        assert "Assignments API" in tags
        
    def test_full_workflow_with_validation_success(self, minimal_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        with patch('builtins.__import__') as mock_import:
            def side_effect(name, *args, **kwargs):
                if name == 'openapi_schema_pydantic':
                    mock_module = Mock()
                    mock_openapi = Mock()
                    mock_openapi.model_validate = Mock(return_value=True)
                    mock_module.OpenAPI = mock_openapi
                    return mock_module
                else:
                    return __import__(name, *args, **kwargs)
            
            mock_import.side_effect = side_effect
            
            spec = generator.generate_spec()
            result = generator.validate_spec()
            
        assert result is True
        
    def test_full_workflow_with_validation_failure(self, minimal_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        with patch('builtins.__import__') as mock_import:
            def side_effect(name, *args, **kwargs):
                if name == 'openapi_schema_pydantic':
                    mock_module = Mock()
                    mock_openapi = Mock()
                    mock_openapi.model_validate = Mock(side_effect=Exception("Invalid spec"))
                    mock_module.OpenAPI = mock_openapi
                    return mock_module
                else:
                    return __import__(name, *args, **kwargs)
            
            mock_import.side_effect = side_effect
            
            spec = generator.generate_spec()
            result = generator.validate_spec()
            
        assert result is False
        
    def test_builder_with_real_parsed_data(self, tmp_path):
        from parse_canvas_markdown import CanvasMarkdownParser, Resource, Endpoint, Parameter
        
        markdown_content = """# Test API

**`GET /api/v1/test/:id`**

**Scope:** `url:GET|/api/v1/test/*`

Get a test resource.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | The test ID |
| include[] | array | Include additional data |

**`POST /api/v1/test`**

**Scope:** `url:POST|/api/v1/test`

Create a test resource.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| name | string | The test name |
| active | boolean | Whether the test is active |
"""
        
        md_file = tmp_path / "test.md"
        md_file.write_text(markdown_content)
        
        parser = CanvasMarkdownParser()
        resource = parser.parse_file(md_file)
        
        assert resource is not None
        assert resource.name == "Test API"
        assert len(resource.endpoints) == 2
        
        builder = OpenAPIBuilder()
        builder.add_resource(resource)
        
        spec = builder.get_spec()
        
        assert len(spec["paths"]) == 2
        assert "/api/v1/test/{id}" in spec["paths"]
        assert "/api/v1/test" in spec["paths"]
        
        get_operation = spec["paths"]["/api/v1/test/{id}"]["get"]
        assert get_operation["operationId"] == "get_test"
        assert get_operation["tags"] == ["Test API"]
        assert len(get_operation["parameters"]) == 3
        
        post_operation = spec["paths"]["/api/v1/test"]["post"]
        assert post_operation["operationId"] == "create_test"
        # POST operation should have parameters but not necessarily requestBody since parameters are in query
        
    def test_end_to_end_with_file_operations(self, minimal_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        output_dir = tmp_path / "output"
        
        (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        saved_files = generator.save_spec(
            output_dir=str(output_dir),
            formats=["json", "yaml"]
        )
        
        json_file = Path(saved_files["json"])
        yaml_file = Path(saved_files["yaml"])
        
        assert json_file.exists()
        assert yaml_file.exists()
        assert json_file.stat().st_size > 0
        assert yaml_file.stat().st_size > 0
        
        with open(json_file, 'r') as f:
            json_spec = json.load(f)
            
        yaml_content = yaml_file.read_text()
        
        assert json_spec["openapi"] == "3.1.0"
        assert "openapi: 3.1.0" in yaml_content or "openapi: '3.1.0'" in yaml_content
        
        assert json_spec["info"]["title"] == "Canvas LMS API"
        assert "Canvas LMS API" in yaml_content
        
        assert len(json_spec["paths"]) > 0
        assert "paths:" in yaml_content
        
    def test_error_handling_in_workflow(self, tmp_path, capsys):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "invalid.md").write_text("This is not a valid API doc")
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        spec = generator.generate_spec()
        
        assert spec["openapi"] == "3.1.0"
        assert len(spec["paths"]) == 0
        
        captured = capsys.readouterr()
        assert "No endpoints found" in captured.out
        
    def test_workflow_with_empty_docs_directory(self, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        
        with pytest.raises(FileNotFoundError, match="No markdown files found"):
            generator.generate_spec()
            
    def test_workflow_preserves_spec_structure(self, minimal_resource_file, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(docs_dir))
        spec = generator.generate_spec()
        
        required_top_level_keys = ["openapi", "info", "servers", "security", "components", "paths"]
        for key in required_top_level_keys:
            assert key in spec
            
        assert "securitySchemes" in spec["components"]
        assert "schemas" in spec["components"]
        
        assert spec["security"] == [{"bearerAuth": []}]
        
        assert len(spec["servers"]) == 1
        assert "canvas_domain" in spec["servers"][0]["variables"]
        
        for path_data in spec["paths"].values():
            for operation in path_data.values():
                assert "security" in operation
                assert operation["security"] == [{"bearerAuth": []}]
