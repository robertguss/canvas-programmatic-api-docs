# Canvas API → Postman Collection & Python SDK Generator

Generate comprehensive Postman collections **and modern Python SDKs** (1,018+ endpoints across 128 Canvas LMS resources) directly from the official Canvas API markdown documentation.

## 🚀 What's New: Python SDK Generation!

This project now generates **production-ready Python SDKs** with full type hints, async support, and automatic authentication:

```python
from canvas_lms_api_client import AuthenticatedClient
from canvas_lms_api_client.api.courses import get_courses

# Initialize client
client = AuthenticatedClient(
    base_url="https://yourschool.instructure.com/api/v1",
    token="your-access-token"
)

# Sync usage
courses = get_courses.sync(client=client)

# Async usage
courses = await get_courses.asyncio(client=client)
```

## Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd canvas-api-postman-master

# Install dependencies
uv venv && uv pip install -e .

# Generate everything (docs → Postman → OpenAPI → Python SDK)
just generate-all
```

This creates:

- `output/canvas_api.postman_collection.json` - Postman collection
- `output/canvas_api.openapi.yaml` - OpenAPI 3.1 specification
- `sdk/` - Complete Python SDK with type hints

## Import into Postman

1. Open Postman → Import → Upload Files
2. Select `output/canvas_api.postman_collection.json`
3. Set environment variables:

| Variable       | Example Value                        |
| -------------- | ------------------------------------ |
| `base_url`     | `https://yourschool.instructure.com` |
| `canvas_token` | `12345~abcdefg...789`                |

## Features

### Postman Collection

- ✅ **1,018+ Canvas API endpoints** organized by resource type
- ✅ **OAuth2 Bearer authentication** pre-configured
- ✅ **Dynamic path variables** (`:course_id`, `:user_id`, etc.)
- ✅ **Query parameters** with descriptions
- ✅ **Request bodies** for POST/PUT/PATCH operations
- ✅ **OAuth scopes** documented in request descriptions

### Python SDK

- ✅ **Modern Python SDK** with full type hints and IDE autocomplete
- ✅ **Async/sync support** - use `asyncio()` or `sync()` methods
- ✅ **Pydantic models** for automatic serialization/deserialization
- ✅ **Bearer token authentication** built-in
- ✅ **234+ data schemas** with validation
- ✅ **Python 3.13+ support** with latest language features

### OpenAPI Specification

- ✅ **OpenAPI 3.1 compliant** specification
- ✅ **JSON Schema validation** for all request/response models
- ✅ **Complete parameter documentation** extracted from markdown
- ✅ **OAuth2 security schemes** properly defined

## Documentation

For detailed usage, development, and API reference, see the [documentation](docs/index.md).

## Available Commands

```bash
# Core workflow
just generate-all      # Complete pipeline: docs → Postman → OpenAPI → SDK
just fetch-docs        # Download latest Canvas API docs
just collection        # Generate Postman collection only
just openapi          # Generate OpenAPI specification only
just sdk              # Generate Python SDK only
just sdk-clean        # Clean regenerate SDK

# Development
just test             # Validate generated collection
just format-docs      # Format markdown files
just docs-serve       # Serve documentation locally
```
