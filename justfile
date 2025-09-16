fetch-docs:
    python get_api_docs_in_markdown.py

collection:
    python create_postman_collection.py

test:
    python test_collection.py

format-docs:
    npx prettier --write "canvas_api_resources/*.md"

docs-serve:
    uv pip install -e ".[dev]" && mkdocs serve

docs-build:
    uv pip install -e ".[dev]" && mkdocs build
