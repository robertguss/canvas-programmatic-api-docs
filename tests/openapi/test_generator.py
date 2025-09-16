import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch, mock_open
from canvas_openapi.generator import CanvasOpenAPIGenerator
from parse_canvas_markdown import Resource, Endpoint, Parameter


class TestCanvasOpenAPIGenerator:
    
    def test_init_with_default_docs_dir(self):
        generator = CanvasOpenAPIGenerator()
        assert generator.docs_dir == Path("data/canvas_api_resources")
        assert generator.parser is not None
        assert generator.builder is not None
        
    def test_init_with_custom_docs_dir(self):
        custom_dir = "/custom/docs"
        generator = CanvasOpenAPIGenerator(docs_dir=custom_dir)
        assert generator.docs_dir == Path(custom_dir)
        
    def test_generate_spec_docs_dir_not_found(self):
        generator = CanvasOpenAPIGenerator(docs_dir="/nonexistent/path")
        with pytest.raises(FileNotFoundError, match="Documentation directory not found"):
            generator.generate_spec()
            
    def test_generate_spec_no_markdown_files(self, tmp_path):
        generator = CanvasOpenAPIGenerator(docs_dir=str(tmp_path))
        
        with pytest.raises(FileNotFoundError, match="No markdown files found"):
            generator.generate_spec()
            
    def test_generate_spec_with_valid_files(self, temp_docs_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            spec = generator.generate_spec()
            
        assert spec["openapi"] == "3.1.0"
        assert spec["info"]["title"] == "Canvas LMS API"
        assert len(spec["paths"]) > 0
        
    def test_generate_spec_with_invalid_files(self, temp_docs_dir):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=None):
            spec = generator.generate_spec()
            
        assert spec["openapi"] == "3.1.0"
        assert len(spec["paths"]) == 0
        
    def test_generate_spec_with_mixed_files(self, temp_docs_dir, sample_resource):
        (temp_docs_dir / "invalid.md").write_text("invalid content")
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        def mock_parse_file(file_path):
            if "users.md" in str(file_path):
                return sample_resource
            return None
            
        with patch.object(generator.parser, 'parse_file', side_effect=mock_parse_file):
            spec = generator.generate_spec()
            
        assert len(spec["paths"]) > 0
        
    def test_generate_spec_with_schemas(self, temp_docs_dir):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        resource_with_schemas = Resource(
            name="Users",
            description="Users API",
            endpoints=[
                Endpoint(name="Get User", method="GET", path="/users/:id", description="Get user")
            ],
            schemas={"User": {"type": "object", "properties": {"id": {"type": "integer"}}}}
        )
        
        with patch.object(generator.parser, 'parse_file', return_value=resource_with_schemas):
            spec = generator.generate_spec()
            
        assert "User" in spec["components"]["schemas"]
        
    def test_generate_spec_handles_parser_exceptions(self, temp_docs_dir, capsys):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', side_effect=Exception("Parse error")):
            spec = generator.generate_spec()
            
        captured = capsys.readouterr()
        assert "Error processing" in captured.out
        assert "Parse error" in captured.out
        
    def test_save_spec_default_formats(self, temp_docs_dir, temp_output_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            saved_files = generator.save_spec(output_dir=str(temp_output_dir))
            
        assert "json" in saved_files
        assert "yaml" in saved_files
        
        json_file = Path(saved_files["json"])
        yaml_file = Path(saved_files["yaml"])
        
        assert json_file.exists()
        assert yaml_file.exists()
        assert json_file.name == "canvas_api.openapi.json"
        assert yaml_file.name == "canvas_api.openapi.yaml"
        
    def test_save_spec_json_only(self, temp_docs_dir, temp_output_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            saved_files = generator.save_spec(
                output_dir=str(temp_output_dir),
                formats=["json"]
            )
            
        assert "json" in saved_files
        assert "yaml" not in saved_files
        
        json_file = Path(saved_files["json"])
        assert json_file.exists()
        
    def test_save_spec_yaml_only(self, temp_docs_dir, temp_output_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            saved_files = generator.save_spec(
                output_dir=str(temp_output_dir),
                formats=["yaml"]
            )
            
        assert "yaml" in saved_files
        assert "json" not in saved_files
        
        yaml_file = Path(saved_files["yaml"])
        assert yaml_file.exists()
        
    def test_save_spec_creates_output_directory(self, temp_docs_dir, tmp_path, sample_resource):
        output_dir = tmp_path / "new_output"
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            generator.save_spec(output_dir=str(output_dir))
            
        assert output_dir.exists()
        assert output_dir.is_dir()
        
    def test_save_spec_json_content_valid(self, temp_docs_dir, temp_output_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            saved_files = generator.save_spec(
                output_dir=str(temp_output_dir),
                formats=["json"]
            )
            
        json_file = Path(saved_files["json"])
        with open(json_file, 'r') as f:
            spec = json.load(f)
            
        assert spec["openapi"] == "3.1.0"
        assert spec["info"]["title"] == "Canvas LMS API"
        
    def test_save_spec_yaml_content_valid(self, temp_docs_dir, temp_output_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            saved_files = generator.save_spec(
                output_dir=str(temp_output_dir),
                formats=["yaml"]
            )
            
        yaml_file = Path(saved_files["yaml"])
        content = yaml_file.read_text()
        
        assert "openapi:" in content
        assert "Canvas LMS API" in content
        
    def test_validate_spec_success(self, temp_docs_dir, sample_resource):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
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
            
            with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
                result = generator.validate_spec()
                
        assert result is True
        
    def test_validate_spec_failure(self, temp_docs_dir, sample_resource, capsys):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch('builtins.__import__') as mock_import:
            def side_effect(name, *args, **kwargs):
                if name == 'openapi_schema_pydantic':
                    mock_module = Mock()
                    mock_openapi = Mock()
                    mock_openapi.model_validate = Mock(side_effect=Exception("Validation error"))
                    mock_module.OpenAPI = mock_openapi
                    return mock_module
                else:
                    return __import__(name, *args, **kwargs)
            
            mock_import.side_effect = side_effect
            
            with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
                result = generator.validate_spec()
                
        assert result is False
        captured = capsys.readouterr()
        assert "validation failed" in captured.out
        assert "Validation error" in captured.out
        
    def test_validate_spec_import_error(self, temp_docs_dir, sample_resource, capsys):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch('builtins.__import__') as mock_import:
            def side_effect(name, *args, **kwargs):
                if name == 'openapi_schema_pydantic':
                    raise ImportError("openapi_schema_pydantic not found")
                else:
                    return __import__(name, *args, **kwargs)
            
            mock_import.side_effect = side_effect
            
            with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
                result = generator.validate_spec()
                
        assert result is True
        captured = capsys.readouterr()
        assert "not available, skipping validation" in captured.out
        
    def test_generate_spec_prints_progress(self, temp_docs_dir, sample_resource, capsys):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        with patch.object(generator.parser, 'parse_file', return_value=sample_resource):
            generator.generate_spec()
            
        captured = capsys.readouterr()
        assert "Scanning Canvas API documentation" in captured.out
        assert "Found 1 API documentation files" in captured.out
        assert "Processing users.md" in captured.out
        assert "Generated OpenAPI spec with:" in captured.out
        
    def test_generate_spec_with_empty_resource(self, temp_docs_dir, capsys):
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        empty_resource = Resource(name="Empty", description="Empty resource", endpoints=[], schemas={})
        
        with patch.object(generator.parser, 'parse_file', return_value=empty_resource):
            generator.generate_spec()
            
        captured = capsys.readouterr()
        assert "No endpoints found" in captured.out
        
    def test_generate_spec_counts_resources_correctly(self, temp_docs_dir, sample_resource):
        (temp_docs_dir / "courses.md").write_text("# Courses API")
        (temp_docs_dir / "assignments.md").write_text("# Assignments API")
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs_dir))
        
        def mock_parse_file(file_path):
            if "users.md" in str(file_path):
                return sample_resource
            elif "courses.md" in str(file_path):
                return Resource(
                    name="Courses",
                    description="Courses API",
                    endpoints=[Endpoint(name="List Courses", method="GET", path="/courses", description="List courses")],
                    schemas={}
                )
            return None
            
        with patch.object(generator.parser, 'parse_file', side_effect=mock_parse_file):
            spec = generator.generate_spec()
            
        assert len(spec["paths"]) == 2
        
    def test_integration_with_real_parser(self, minimal_resource_file, temp_output_dir):
        temp_docs = temp_output_dir / "docs"
        temp_docs.mkdir()
        (temp_docs / "users.md").write_text(minimal_resource_file.read_text())
        
        generator = CanvasOpenAPIGenerator(docs_dir=str(temp_docs))
        
        spec = generator.generate_spec()
        
        assert spec["openapi"] == "3.1.0"
        assert len(spec["paths"]) > 0
        
        saved_files = generator.save_spec(output_dir=str(temp_output_dir))
        
        json_file = Path(saved_files["json"])
        assert json_file.exists()
        
        with open(json_file, 'r') as f:
            saved_spec = json.load(f)
            
        assert saved_spec == spec
