# Usage Guide

This guide covers how to generate and use Canvas API Postman collections, OpenAPI specifications, and Python SDKs.

## What Gets Generated

This project generates three main outputs:

### 1. Postman Collection
- **1,018 API endpoints** across **128 resource categories**
- Proper OAuth2 Bearer token authentication
- Path variables for dynamic URLs (e.g., `:course_id`, `:user_id`)
- Query parameters with descriptions
- Request body parameters for POST/PUT/PATCH requests
- OAuth scopes documented in request descriptions

### 2. OpenAPI Specification
- **OpenAPI 3.1 compliant** specification
- **234+ data schemas** with JSON Schema validation
- Complete parameter documentation
- OAuth2 security schemes
- Available in both YAML and JSON formats

### 3. Python SDK
- **Modern Python SDK** with full type hints
- **Async/sync support** for all endpoints
- **Pydantic models** for automatic validation
- **Bearer token authentication** built-in
- **IDE autocomplete** support

## Quick Start

### Option 1: Generate Everything

```bash
# Install dependencies
uv sync

# Generate everything: Postman + OpenAPI + Python SDK
just generate-all
```

This creates:
- `output/canvas_api.postman_collection.json` - Postman collection
- `output/canvas_api.openapi.yaml` - OpenAPI specification
- `sdk/canvas_lms_api_client/` - Python SDK

### Option 2: Generate Individual Components

```bash
# Generate only Postman collection
just collection

# Generate only OpenAPI specification
just openapi

# Generate only Python SDK
just sdk
```

## Using the Generated Tools

### Postman Collection

1. **Import into Postman**
   - Open Postman
   - Click **Import** button
   - Select the generated `canvas_api.postman_collection.json` file
   - The collection will be imported with all 128 resource folders

2. **Configure Authentication**
   - Go to the collection's **Variables** tab
   - Set `base_url` to your Canvas instance (e.g., `https://your-school.instructure.com`)
   - Set `access_token` to your Canvas API token

### Python SDK

1. **Install the SDK**
   ```bash
   cd sdk
   pip install -e .
   ```

2. **Basic Usage**
   ```python
   from canvas_lms_api_client import AuthenticatedClient
   from canvas_lms_api_client.api.courses import get_courses
   
   # Initialize client
   client = AuthenticatedClient(
       base_url="https://yourschool.instructure.com/api/v1",
       token="your-canvas-access-token"
   )
   
   # Get all courses
   courses = get_courses.sync(client=client)
   print(f"Found {len(courses)} courses")
   ```

3. **Async Usage**
   ```python
   import asyncio
   
   async def main():
       courses = await get_courses.asyncio(client=client)
       print(f"Found {len(courses)} courses")
   
   asyncio.run(main())
   ```

### OpenAPI Specification

1. **Generate Documentation**
   ```bash
   # Using Swagger UI
   npx swagger-ui-serve output/canvas_api.openapi.yaml
   
   # Using Redoc
   npx redoc-cli serve output/canvas_api.openapi.yaml
   ```

2. **Generate Other Language Clients**
   ```bash
   # Generate JavaScript client
   openapi-generator-cli generate \
     -i output/canvas_api.openapi.yaml \
     -g javascript \
     -o clients/javascript
   ```

## Collection Structure

```
Canvas API (Generated from Markdown)
├── Access Tokens (4 endpoints)
├── Accounts (20 endpoints)
├── Assignments (20 endpoints)
├── Courses (30 endpoints)
├── Discussion Topics (58 endpoints)
├── Files (53 endpoints)
├── Submissions (46 endpoints)
├── Users (43 endpoints)
└── ... (120 more resource folders)
```

## Features

### Authentication
- Collection-level OAuth2 Bearer token authentication
- All requests inherit authentication from the collection
- Easy token management through collection variables

### Path Variables
- Canvas path parameters like `:course_id` are automatically detected
- Postman variables are created for each path parameter
- Example values provided for easy testing

### Query Parameters
- Query parameters extracted from documentation tables
- Optional parameters are disabled by default
- Parameter descriptions included for reference

### Request Bodies
- POST/PUT/PATCH requests include form-data bodies
- Parameters extracted from documentation
- Required vs optional parameters properly marked

## Scripts Overview

### `parse_canvas_markdown.py`
- Parses 128 markdown files in `data/canvas_api_resources/`
- Extracts endpoints, parameters, scopes, and descriptions
- Uses popular Python libraries: `markdown`, `beautifulsoup4`, `pydantic`

### `create_postman_collection.py`
- Generates Postman v2.1 collection format
- Creates proper folder structure and request objects
- Handles authentication and variable setup

### `test_collection.py`
- Validates the generated collection
- Provides statistics and sample data
- Useful for debugging and verification

## Updating the Collection

To get the latest Canvas API endpoints:

```bash
# Fetch latest API documentation
just fetch-docs

# Regenerate the collection
python create_postman_collection.py
```

## Troubleshooting

### Missing Endpoints
If you notice missing endpoints, check:
1. The markdown files in `data/canvas_api_resources/`
2. The endpoint regex pattern in `parse_canvas_markdown.py`
3. Run `python parse_canvas_markdown.py` to see parsing results

### Authentication Issues
- Ensure your Canvas token has appropriate scopes
- Check that `base_url` points to your Canvas instance
- Verify the token is set in collection variables, not individual requests

### Parameter Issues
- Parameters are extracted from markdown tables
- Path parameters are auto-detected from URL patterns
- Body parameters are included for POST/PUT/PATCH requests

## Collection Statistics

- **Total Endpoints**: 1,018
- **Resource Categories**: 128
- **Authentication**: OAuth2 Bearer Token
- **Format**: Postman Collection v2.1
- **Generated From**: Canvas API Markdown Documentation

## Advanced Usage

### Custom Base URL

You can override the base URL for specific environments:

1. Create a new environment in Postman
2. Set `base_url` variable to your Canvas instance
3. Select the environment when making requests

### Bulk Testing

Use Postman's Collection Runner to test multiple endpoints:

1. Select the Canvas API collection
2. Click **Run** to open Collection Runner
3. Choose specific folders or endpoints to test
4. Configure iterations and delays as needed

### Environment Variables

Common variables you might want to set:

| Variable | Description | Example |
|----------|-------------|---------|
| `base_url` | Canvas instance URL | `https://school.instructure.com` |
| `access_token` | Canvas API token | `12345~abcdef...` |
| `course_id` | Course ID for testing | `123456` |
| `user_id` | User ID for testing | `789012` |
| `assignment_id` | Assignment ID for testing | `345678` |

### Request Customization

Each request can be customized:

- **Headers**: Add custom headers as needed
- **Parameters**: Enable/disable query parameters
- **Body**: Modify form data for POST/PUT requests
- **Tests**: Add JavaScript tests for response validation

## Next Steps

1. **Import the collection** into Postman
2. **Set your credentials** in collection variables
3. **Start testing** Canvas API endpoints
4. **Customize requests** as needed for your use case

The collection provides a solid foundation for Canvas API development and testing!
