# Canvas API → Postman Collection Generator

Generate a comprehensive Postman collection (1,018+ endpoints across 128 Canvas LMS resources) directly from the official Canvas API markdown documentation.

## Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd canvas-api-postman-master

# Install dependencies
uv venv && uv pip install -e .
# OR using pip: pip install -e .

# Generate Postman collection
just collection
```

This creates `output/canvas_api.postman_collection.json` ready for import into Postman.

## Import into Postman

1. Open Postman → Import → Upload Files
2. Select `output/canvas_api.postman_collection.json`
3. Set environment variables:

| Variable | Example Value |
|----------|---------------|
| `base_url` | `https://yourschool.instructure.com` |
| `canvas_token` | `12345~abcdefg...789` |

## Features

- ✅ **1,018+ Canvas API endpoints** organized by resource type
- ✅ **OAuth2 Bearer authentication** pre-configured
- ✅ **Dynamic path variables** (`:course_id`, `:user_id`, etc.)
- ✅ **Query parameters** with descriptions
- ✅ **Request bodies** for POST/PUT/PATCH operations
- ✅ **OAuth scopes** documented in request descriptions

## Documentation

For detailed usage, development, and API reference, see the [documentation](docs/index.md).

## Available Commands

```bash
just fetch-docs     # Download latest Canvas API docs
just collection     # Generate Postman collection
just test          # Validate generated collection
just format-docs   # Format markdown files
just docs-serve    # Serve documentation locally
```
