fetch-docs:
    python get_api_docs_in_markdown.py

collection:
    python create_postman_collection.py

test:
    uv pip install -e ".[test]"
    pytest -q

cov:
    uv pip install -e ".[test]"
    pytest --cov --cov-report=term-missing

cov-html:
    uv pip install -e ".[test]"
    pytest --cov --cov-report=term-missing --cov-report=html
    open htmlcov/index.html

postman-test:
    python test_collection.py

format-md:
    npx prettier --write "**/*.md"

docs-serve:
    uv pip install -e ".[dev]" && mkdocs serve

docs-build:
    uv pip install -e ".[dev]" && mkdocs build

# OpenAPI and SDK generation
openapi:
    python generate_openapi.py

openapi-validate:
    python generate_openapi.py --validate

sdk:
    python generate_sdk.py

sdk-clean:
    python generate_sdk.py --clean --regenerate-spec

# Full workflow
generate-all: fetch-docs collection openapi sdk
    @echo "🎉 Generated Postman collection, OpenAPI spec, and Python SDK!"
