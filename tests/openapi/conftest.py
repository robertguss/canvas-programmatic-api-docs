import pytest
import json
from pathlib import Path
from unittest.mock import Mock, MagicMock
from parse_canvas_markdown import Resource, Endpoint, Parameter
from canvas_openapi.builder import OpenAPIBuilder
from canvas_openapi.generator import CanvasOpenAPIGenerator


@pytest.fixture
def fixtures_dir():
    return Path(__file__).parent.parent / "fixtures"


@pytest.fixture
def minimal_resource_file(fixtures_dir):
    return fixtures_dir / "minimal_resource.md"


@pytest.fixture
def invalid_resource_file(fixtures_dir):
    return fixtures_dir / "invalid_resource.md"


@pytest.fixture
def complex_resource_file(fixtures_dir):
    return fixtures_dir / "complex_resource.md"


@pytest.fixture
def sample_parameter():
    return Parameter(
        name="user_id",
        type="integer",
        description="The ID of the user",
        required=True,
        location="path"
    )


@pytest.fixture
def sample_endpoint():
    return Endpoint(
        name="Get User",
        method="GET",
        path="/api/v1/users/:id",
        description="Get details for a single user",
        scope="url:GET|/api/v1/users/*",
        parameters=[
            Parameter(
                name="id",
                type="integer", 
                description="User ID",
                required=True,
                location="path"
            ),
            Parameter(
                name="include",
                type="array",
                description="Include additional information",
                required=False,
                location="query",
                enum_values=["profile", "avatar_url", "permissions"]
            )
        ]
    )


@pytest.fixture
def sample_resource(sample_endpoint):
    return Resource(
        name="Users",
        description="The Users API allows you to manage users in Canvas.",
        endpoints=[sample_endpoint],
        schemas={"User": {"type": "object", "properties": {"id": {"type": "integer"}}}}
    )


@pytest.fixture
def openapi_builder():
    return OpenAPIBuilder()


@pytest.fixture
def mock_parser():
    parser = Mock()
    parser.parse_file = Mock()
    return parser


@pytest.fixture
def mock_builder():
    builder = Mock()
    builder.add_resource = Mock()
    builder.add_schemas = Mock()
    builder.get_spec = Mock(return_value={
        "openapi": "3.1.0",
        "info": {"title": "Test API", "version": "1.0.0"},
        "paths": {},
        "components": {"schemas": {}}
    })
    builder.to_yaml = Mock(return_value="openapi: 3.1.0\ninfo:\n  title: Test API")
    return builder


@pytest.fixture
def openapi_generator(tmp_path):
    return CanvasOpenAPIGenerator(docs_dir=str(tmp_path))


@pytest.fixture
def sample_openapi_spec():
    return {
        "openapi": "3.1.0",
        "info": {
            "title": "Canvas LMS API",
            "description": "The Canvas LMS REST API",
            "version": "1.0.0"
        },
        "servers": [
            {
                "url": "https://{canvas_domain}/api/v1",
                "description": "Canvas LMS API Server"
            }
        ],
        "paths": {
            "/users/{id}": {
                "get": {
                    "summary": "Get User",
                    "operationId": "get_users",
                    "tags": ["Users"],
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "responses": {
                        "200": {"description": "Successful response"}
                    }
                }
            }
        },
        "components": {
            "schemas": {},
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer"
                }
            }
        }
    }


@pytest.fixture
def temp_docs_dir(tmp_path, minimal_resource_file):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    
    (docs_dir / "users.md").write_text(minimal_resource_file.read_text())
    
    return docs_dir


@pytest.fixture
def temp_output_dir(tmp_path):
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir
