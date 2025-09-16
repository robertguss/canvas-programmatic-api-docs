import json
import uuid
from pathlib import Path
from unittest.mock import patch, mock_open
import pytest
from create_postman_collection import PostmanCollectionGenerator
from parse_canvas_markdown import Resource, Endpoint, Parameter


class TestPostmanCollectionGenerator:
    
    def test_init_default_values(self):
        generator = PostmanCollectionGenerator()
        assert generator.base_url == "{{base_url}}"
        assert generator.access_token == "{{access_token}}"
        assert isinstance(generator.collection_id, str)
        assert len(generator.collection_id) == 36
    
    def test_init_with_custom_uuid(self):
        test_uuid = "test-uuid-123"
        with patch('create_postman_collection.uuid.uuid4', return_value=test_uuid):
            generator = PostmanCollectionGenerator()
            assert generator.collection_id == test_uuid
    
    def test_convert_path_to_postman(self):
        generator = PostmanCollectionGenerator()
        
        test_cases = [
            ("/api/v1/courses", "/api/v1/courses"),
            ("/api/v1/courses/:course_id", "/api/v1/courses/:course_id"),
            ("/api/v1/accounts/:account_id/courses", "/api/v1/accounts/:account_id/courses"),
            ("courses/:id/files/:file_id", "courses/:id/files/:file_id"),
        ]
        
        for input_path, expected in test_cases:
            assert generator._convert_path_to_postman(input_path) == expected
    
    def test_build_url_object_simple_path(self):
        generator = PostmanCollectionGenerator()
        path = "/api/v1/courses"
        parameters = []
        
        result = generator._build_url_object(path, parameters)
        
        expected = {
            "raw": "{{base_url}}/api/v1/courses",
            "host": ["{{base_url}}"],
            "path": ["api", "v1", "courses"]
        }
        
        assert result == expected
    
    def test_build_url_object_with_path_params(self):
        generator = PostmanCollectionGenerator()
        path = "/api/v1/courses/:course_id"
        parameters = [
            Parameter(name="course_id", location="path", type="string", description="Course ID", required=True)
        ]
        
        result = generator._build_url_object(path, parameters)
        
        assert result["raw"] == "{{base_url}}/api/v1/courses/:course_id"
        assert result["host"] == ["{{base_url}}"]
        assert result["path"] == ["api", "v1", "courses", ":course_id"]
        assert "variable" in result
        assert len(result["variable"]) == 1
        assert result["variable"][0]["key"] == "course_id"
    
    def test_build_url_object_with_query_params(self):
        generator = PostmanCollectionGenerator()
        path = "/api/v1/courses"
        parameters = [
            Parameter(name="include", location="query", type="string", description="Include data", required=False),
            Parameter(name="per_page", location="query", type="integer", description="Items per page", required=False)
        ]
        
        result = generator._build_url_object(path, parameters)
        
        assert "query" in result
        assert len(result["query"]) == 2
        
        include_param = next(p for p in result["query"] if p["key"] == "include")
        assert include_param["disabled"] is True
        
        per_page_param = next(p for p in result["query"] if p["key"] == "per_page")
        assert per_page_param["disabled"] is True
    
    def test_build_request_body_get_method(self):
        generator = PostmanCollectionGenerator()
        endpoint = Endpoint(
            method="GET",
            path="/api/v1/courses",
            name="List Courses",
            description="Get all courses",
            parameters=[]
        )
        
        result = generator._build_request_body(endpoint)
        assert result is None
    
    def test_build_request_body_post_with_body_params(self):
        generator = PostmanCollectionGenerator()
        endpoint = Endpoint(
            method="POST",
            path="/api/v1/courses",
            name="Create Course",
            description="Create a new course",
            parameters=[
                Parameter(name="course[name]", location="body", type="string", description="Course name", required=True),
                Parameter(name="course[code]", location="body", type="string", description="Course code", required=False)
            ]
        )
        
        result = generator._build_request_body(endpoint)
        
        assert result is not None
        assert result["mode"] == "formdata"
        assert "formdata" in result
        assert len(result["formdata"]) == 2
        
        name_param = next(p for p in result["formdata"] if p["key"] == "course[name]")
        assert name_param["disabled"] is False
        
        code_param = next(p for p in result["formdata"] if p["key"] == "course[code]")
        assert code_param["disabled"] is True
    
    def test_create_request_item(self):
        generator = PostmanCollectionGenerator()
        endpoint = Endpoint(
            method="GET",
            path="/api/v1/courses/:course_id",
            name="Get Course",
            description="Get course details",
            scope="url:GET|/api/v1/courses/*",
            parameters=[
                Parameter(name="course_id", location="path", type="string", description="Course ID", required=True)
            ]
        )
        
        result = generator._create_request_item(endpoint)
        
        assert result["name"] == "Get Course"
        assert result["request"]["method"] == "GET"
        assert result["request"]["url"]["raw"] == "{{base_url}}/api/v1/courses/:course_id"
        assert "OAuth Scope:" in result["request"]["description"]
    
    def test_create_resource_folder(self):
        generator = PostmanCollectionGenerator()
        resource = Resource(
            name="Courses",
            description="Course management API",
            endpoints=[
                Endpoint(method="GET", path="/api/v1/courses", name="List Courses", description="Get all courses"),
                Endpoint(method="POST", path="/api/v1/courses", name="Create Course", description="Create course")
            ]
        )
        
        result = generator._create_resource_folder(resource)
        
        assert result["name"] == "Courses"
        assert result["description"] == "Course management API"
        assert len(result["item"]) == 2
        assert result["item"][0]["name"] == "List Courses"
        assert result["item"][1]["name"] == "Create Course"
    
    def test_generate_collection(self):
        generator = PostmanCollectionGenerator()
        resources = {
            "courses": Resource(
                name="Courses",
                description="Course API",
                endpoints=[
                    Endpoint(method="GET", path="/api/v1/courses", name="List Courses", description="Get courses")
                ]
            )
        }
        
        result = generator.generate_collection(resources)
        
        assert "info" in result
        assert result["info"]["name"] == "Canvas API (Generated from Markdown)"
        assert "auth" in result
        assert result["auth"]["type"] == "bearer"
        assert "variable" in result
        assert len(result["variable"]) == 2
        assert "item" in result
        assert len(result["item"]) == 1
        assert result["item"][0]["name"] == "Courses"
    
    def test_save_collection(self, tmp_path):
        generator = PostmanCollectionGenerator()
        collection = {"test": "data"}
        output_path = tmp_path / "test_collection.json"
        
        generator.save_collection(collection, output_path)
        
        assert output_path.exists()
        with open(output_path, 'r') as f:
            saved_data = json.load(f)
        assert saved_data == collection


class TestMainFunction:
    
    @patch('create_postman_collection.parse_all_resources')
    @patch('create_postman_collection.Path')
    def test_main_no_resources_dir(self, mock_path, mock_parse):
        mock_path.return_value.exists.return_value = False
        
        with patch('builtins.print') as mock_print:
            from create_postman_collection import main
            main()
            
        mock_print.assert_called()
        assert any("Error: Resources directory not found" in str(call) for call in mock_print.call_args_list)
    
    @patch('create_postman_collection.parse_all_resources')
    @patch('create_postman_collection.Path')
    def test_main_no_resources_found(self, mock_path, mock_parse):
        mock_path.return_value.exists.return_value = True
        mock_parse.return_value = {}
        
        with patch('builtins.print') as mock_print:
            from create_postman_collection import main
            main()
            
        mock_print.assert_called()
        assert any("No resources found to parse!" in str(call) for call in mock_print.call_args_list)
    
    @patch('create_postman_collection.parse_all_resources')
    @patch('create_postman_collection.Path')
    @patch('create_postman_collection.PostmanCollectionGenerator')
    def test_main_success(self, mock_generator_class, mock_path, mock_parse):
        mock_path.return_value.exists.return_value = True
        mock_parse.return_value = {
            "courses": Resource(
                name="Courses",
                description="Course API",
                endpoints=[Endpoint(method="GET", path="/api/v1/courses", name="List", description="List")]
            )
        }
        
        mock_generator = mock_generator_class.return_value
        mock_generator.generate_collection.return_value = {"item": [{"name": "Courses"}]}
        
        with patch('builtins.print') as mock_print:
            from create_postman_collection import main
            main()
            
        mock_generator.generate_collection.assert_called_once()
        mock_generator.save_collection.assert_called_once()
        mock_print.assert_called()
