# Usage Guide

This guide covers how to generate and use Canvas API Postman collections.

## Generated Collection

The generated collection includes:
- **1,018 API endpoints** across **128 resource categories**
- Proper OAuth2 Bearer token authentication
- Path variables for dynamic URLs (e.g., `:course_id`, `:user_id`)
- Query parameters with descriptions
- Request body parameters for POST/PUT/PATCH requests
- OAuth scopes documented in request descriptions

## Quick Start

### 1. Generate the Collection

```bash
# Install dependencies
uv sync

# Generate the Postman collection
python create_postman_collection.py
```

This creates `output/canvas_api.postman_collection.json`

### 2. Import into Postman

1. Open Postman
2. Click **Import** button
3. Select the generated `canvas_api.postman_collection.json` file
4. The collection will be imported with all 128 resource folders

### 3. Configure Authentication

After importing, set up your Canvas credentials:

1. Go to the collection's **Variables** tab
2. Set `base_url` to your Canvas instance (e.g., `https://your-school.instructure.com`)
3. Set `access_token` to your Canvas API token

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
