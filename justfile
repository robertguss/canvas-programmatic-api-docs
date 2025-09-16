fetch-docs:
    python get_api_docs_in_markdown.py

update-docs: fetch-docs

sync-docs: fetch-docs
