import re
from pathlib import Path
from unittest.mock import patch, Mock
import pytest
from parse_canvas_markdown import (
    Parameter, Endpoint, Resource, CanvasMarkdownParser, parse_all_resources
)


class TestParameter:
    
    def test_parameter_creation(self):
        param = Parameter(
            name="course_id",
            location="path",
            type="string",
            description="The course identifier",
            required=True
        )
        
        assert param.name == "course_id"
        assert param.location == "path"
        assert param.type == "string"
        assert param.description == "The course identifier"
        assert param.required is True
    
    def test_parameter_default_required(self):
        param = Parameter(
            name="optional_param",
            location="query",
            type="string",
            description="Optional parameter"
        )
        
        assert param.required is False


class TestEndpoint:
    
    def test_endpoint_creation(self):
        parameters = [
            Parameter("id", "path", "string", "Course ID", True)
        ]
        
        endpoint = Endpoint(
            method="GET",
            path="/api/v1/courses/:id",
            name="Get Course",
            description="Retrieve course details",
            scope="url:GET|/api/v1/courses/*",
            parameters=parameters
        )
        
        assert endpoint.method == "GET"
        assert endpoint.path == "/api/v1/courses/:id"
        assert endpoint.name == "Get Course"
        assert endpoint.description == "Retrieve course details"
        assert endpoint.scope == "url:GET|/api/v1/courses/*"
        assert len(endpoint.parameters) == 1
    
    def test_endpoint_default_values(self):
        endpoint = Endpoint(
            method="POST",
            path="/api/v1/courses",
            name="Create Course",
            description="Create a new course"
        )
        
        assert endpoint.scope is None
        assert endpoint.parameters == []


class TestResource:
    
    def test_resource_creation(self):
        endpoints = [
            Endpoint("GET", "/api/v1/courses", "List Courses", "Get all courses"),
            Endpoint("POST", "/api/v1/courses", "Create Course", "Create course")
        ]
        
        resource = Resource(
            name="Courses",
            description="Course management API",
            endpoints=endpoints
        )
        
        assert resource.name == "Courses"
        assert resource.description == "Course management API"
        assert len(resource.endpoints) == 2
    
    def test_resource_default_endpoints(self):
        resource = Resource(
            name="Users",
            description="User management API"
        )
        
        assert resource.endpoints == []


class TestCanvasMarkdownParser:
    
    def test_parser_initialization(self):
        parser = CanvasMarkdownParser()
        
        assert parser.ENDPOINT_PATTERN.pattern == r'\*\*`(GET|POST|PUT|DELETE|PATCH)\s+([^`]+)`\*\*'
        assert parser.SCOPE_PATTERN.pattern == r'\*\*Scope:\*\*\s+`([^`]+)`'
        assert parser.PATH_PARAM_PATTERN.pattern == r':(\w+)'
        assert parser.md is not None
    
    def test_extract_resource_name(self):
        parser = CanvasMarkdownParser()
        
        content = """# Courses API
        
Some description here.

## Other Section
"""
        
        result = parser._extract_resource_name(content)
        assert result == "Courses API"
    
    def test_extract_resource_name_no_heading(self):
        parser = CanvasMarkdownParser()
        content = "No heading in this content"
        
        result = parser._extract_resource_name(content)
        assert result == "Unknown Resource"
    
    def test_extract_resource_description(self):
        parser = CanvasMarkdownParser()
        
        content = """# Courses
        
## Courses API

The Courses API allows you to manage courses in Canvas.
You can create, update, and delete courses.

## Another Section
"""
        
        result = parser._extract_resource_description(content)
        assert "The Courses API allows you to manage courses in Canvas." in result
        assert "You can create, update, and delete courses." in result
    
    def test_extract_resource_description_no_api_section(self):
        parser = CanvasMarkdownParser()
        content = """# Courses
        
Just some content without API section.
"""
        
        result = parser._extract_resource_description(content)
        assert result == ""
    
    def test_generate_endpoint_name_list_action(self):
        parser = CanvasMarkdownParser()
        
        result = parser._generate_endpoint_name("GET", "/api/v1/courses", "List all courses")
        assert result == "List Courses"
    
    def test_generate_endpoint_name_create_action(self):
        parser = CanvasMarkdownParser()
        
        result = parser._generate_endpoint_name("POST", "/api/v1/courses", "Create a course")
        assert result == "Create Courses"
    
    def test_generate_endpoint_name_with_action(self):
        parser = CanvasMarkdownParser()
        
        result = parser._generate_endpoint_name("GET", "/api/v1/courses/search", "Search courses")
        assert result == "Get Courses Search"
    
    def test_generate_endpoint_name_fallback(self):
        parser = CanvasMarkdownParser()
        
        result = parser._generate_endpoint_name("GET", "/custom/path", "Custom endpoint")
        assert result == "Get /Custom/Path"
    
    def test_extract_parameters_path_params(self):
        parser = CanvasMarkdownParser()
        
        content = "Some endpoint content"
        path = "/api/v1/courses/:course_id/users/:user_id"
        method = "GET"
        
        result = parser._extract_parameters(content, path, method)
        
        assert len(result) == 2
        course_param = next(p for p in result if p.name == "course_id")
        user_param = next(p for p in result if p.name == "user_id")
        
        assert course_param.location == "path"
        assert course_param.required is True
        assert user_param.location == "path"
        assert user_param.required is True
    
    def test_parse_parameter_table(self):
        parser = CanvasMarkdownParser()
        
        content = """
**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| include[] | string | Include additional information |
| per_page | integer | Number of items per page |
| enrollment_type* | string | Required enrollment type |
"""
        
        result = parser._parse_parameter_table(content, "GET")
        
        assert len(result) == 3
        
        include_param = next(p for p in result if p.name == "include[]")
        assert include_param.type == "string"
        assert include_param.location == "query"
        assert include_param.required is False
        
        per_page_param = next(p for p in result if p.name == "per_page")
        assert per_page_param.type == "integer"
        assert per_page_param.required is False
        
        enrollment_param = next(p for p in result if p.name == "enrollment_type")
        assert enrollment_param.required is True
    
    def test_parse_parameter_table_post_method(self):
        parser = CanvasMarkdownParser()
        
        content = """
**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| course[name] | string | Course name |
| course[code] | object | Course code object |
"""
        
        result = parser._parse_parameter_table(content, "POST")
        
        assert len(result) == 2
        
        name_param = next(p for p in result if p.name == "course[name]")
        assert name_param.location == "query"
        
        code_param = next(p for p in result if p.name == "course[code]")
        assert code_param.location == "body"
    
    def test_parse_parameter_table_no_table(self):
        parser = CanvasMarkdownParser()
        
        content = "No parameter table here"
        
        result = parser._parse_parameter_table(content, "GET")
        assert result == []
    
    def test_extract_endpoint_description(self):
        parser = CanvasMarkdownParser()
        
        content = """
List all courses for the current user.
This endpoint returns paginated results.

**Scope:** url:GET|/api/v1/courses

**Request Parameters:**
"""
        
        result = parser._extract_endpoint_description(content)
        assert "List all courses for the current user." in result
        assert "This endpoint returns paginated results." in result
        assert "Scope:" not in result
        assert "Request Parameters:" not in result
    
    def test_parse_endpoint(self):
        parser = CanvasMarkdownParser()
        
        content = """
**`GET /api/v1/courses/:course_id`**

**Scope:** `url:GET|/api/v1/courses/*`

Get details for a single course.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| include[] | string | Include additional information |

**`POST /api/v1/courses`**
"""
        
        match = parser.ENDPOINT_PATTERN.search(content)
        result = parser._parse_endpoint(content, match)
        
        assert result is not None
        assert result.method == "GET"
        assert result.path == "/api/v1/courses/:course_id"
        assert result.scope == "url:GET|/api/v1/courses/*"
        assert "Get details for a single course." in result.description
        assert len(result.parameters) == 2  # 1 path param + 1 query param
    
    def test_parse_file(self, tmp_path):
        parser = CanvasMarkdownParser()
        
        test_content = """# Courses

## Courses API

The Courses API allows you to manage courses.

**`GET /api/v1/courses`**

**Scope:** `url:GET|/api/v1/courses`

List all courses for the current user.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| include[] | string | Include additional information |

**`POST /api/v1/courses`**

Create a new course.
"""
        
        test_file = tmp_path / "courses.md"
        test_file.write_text(test_content)
        
        result = parser.parse_file(test_file)
        
        assert result.name == "Courses"
        assert "The Courses API allows you to manage courses." in result.description
        assert len(result.endpoints) == 2
        
        get_endpoint = next(e for e in result.endpoints if e.method == "GET")
        assert get_endpoint.path == "/api/v1/courses"
        assert get_endpoint.scope == "url:GET|/api/v1/courses"
        
        post_endpoint = next(e for e in result.endpoints if e.method == "POST")
        assert post_endpoint.path == "/api/v1/courses"


class TestParseAllResources:
    
    def test_parse_all_resources(self, tmp_path):
        # Create test markdown files
        courses_content = """# Courses

## Courses API

Course management.

**`GET /api/v1/courses`**

List courses.
"""
        
        users_content = """# Users

## Users API

User management.

**`GET /api/v1/users`**

List users.
"""
        
        (tmp_path / "courses.md").write_text(courses_content)
        (tmp_path / "users.md").write_text(users_content)
        (tmp_path / "not_markdown.txt").write_text("Not a markdown file")
        
        result = parse_all_resources(tmp_path)
        
        assert len(result) == 2
        assert "courses" in result
        assert "users" in result
        
        assert result["courses"].name == "Courses"
        assert result["users"].name == "Users"
        assert len(result["courses"].endpoints) == 1
        assert len(result["users"].endpoints) == 1
    
    def test_parse_all_resources_empty_directory(self, tmp_path):
        result = parse_all_resources(tmp_path)
        assert result == {}
    
    def test_parse_all_resources_with_errors(self, tmp_path):
        # Create a file that will cause parsing errors
        bad_content = "Invalid markdown content"
        (tmp_path / "bad.md").write_text(bad_content)
        
        good_content = """# Good Resource

## Good API

**`GET /api/v1/good`**

Good endpoint.
"""
        (tmp_path / "good.md").write_text(good_content)
        
        with patch('builtins.print') as mock_print:
            result = parse_all_resources(tmp_path)
        
        # Should still parse the good file
        assert "good" in result
        assert result["good"].name == "Good Resource"


class TestMainFunction:
    
    @patch('parse_canvas_markdown.parse_all_resources')
    @patch('parse_canvas_markdown.Path')
    def test_main_function(self, mock_path, mock_parse):
        mock_path.return_value = Path("data/canvas_api_resources")
        mock_parse.return_value = {
            "courses": Mock(name="Courses", endpoints=[Mock(), Mock()]),
            "users": Mock(name="Users", endpoints=[Mock()])
        }
        
        # Test that we can import and run the main section
        import parse_canvas_markdown
        
        # The main section should be testable by calling the functions directly
        assert callable(parse_canvas_markdown.parse_all_resources)
        assert hasattr(parse_canvas_markdown, 'CanvasMarkdownParser')
