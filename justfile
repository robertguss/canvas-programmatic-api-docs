fetch-docs:
    python get_api_docs_in_markdown.py

collection:
    python create_postman_collection.py

test:
    python test_collection.py

format-md:
    npx prettier --write "**/*.md"

docs-serve:
    uv pip install -e ".[dev]" && mkdocs serve

docs-build:
    uv pip install -e ".[dev]" && mkdocs build
