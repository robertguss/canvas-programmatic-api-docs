fetch-docs:
    python get_api_docs_in_markdown.py

format-docs:
    npx prettier --write "canvas_api_resources/*.md"
