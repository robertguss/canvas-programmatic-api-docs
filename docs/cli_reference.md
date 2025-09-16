# CLI Reference

This page documents all command-line interfaces and available commands for the Canvas API Postman Collection Generator.

## Just Commands

The project uses [just](https://github.com/casey/just) for task automation. All commands should be run from the project root directory.

### Core Commands

#### `just fetch-docs`
Download the latest Canvas API documentation from the official Canvas API docs site.

```bash
just fetch-docs
```

**What it does:**
- Runs `python get_api_docs_in_markdown.py`
- Downloads all Canvas API resource documentation
- Saves markdown files to `canvas_api_resources/`
- Overwrites existing files with latest versions

**Output:**
- Creates/updates 128+ markdown files in `canvas_api_resources/`
- Prints progress for each downloaded resource

#### `just collection`
Generate the Postman collection from Canvas API markdown documentation.

```bash
just collection
```

**What it does:**
- Runs `python create_postman_collection.py`
- Parses all markdown files in `canvas_api_resources/`
- Generates `output/canvas_api.postman_collection.json`
- Creates organized folder structure with 1,018+ endpoints

**Output:**
- `output/canvas_api.postman_collection.json` - Ready for Postman import
- Console output showing parsing progress and statistics

#### `just test`
Validate the generated Postman collection.

```bash
just test
```

**What it does:**
- Runs `python test_collection.py`
- Validates JSON structure and format
- Checks authentication configuration
- Verifies endpoint counts and organization

**Output:**
- Collection validation results
- Statistics about endpoints, folders, and parameters
- Error messages if validation fails

### Documentation Commands

#### `just docs-serve`
Start a local documentation server with auto-reload.

```bash
just docs-serve
```

**What it does:**
- Installs documentation dependencies if needed
- Starts MkDocs development server
- Serves documentation at `http://localhost:8000`
- Auto-reloads when documentation files change

**Requirements:**
- MkDocs and dependencies installed (`uv pip install -e ".[dev]"`)

#### `just format-docs`
Format markdown documentation files using Prettier.

```bash
just format-docs
```

**What it does:**
- Runs `npx prettier --write "**/*.md"`
- Formats all markdown files in the project
- Ensures consistent markdown formatting

**Requirements:**
- Node.js and npm installed
- Prettier available via npx

## Python Scripts

### `create_postman_collection.py`

Main script for generating Postman collections.

```bash
python create_postman_collection.py [options]
```

**Options:**
- Currently no command-line options (uses defaults)
- Reads from `canvas_api_resources/` directory
- Outputs to `output/canvas_api.postman_collection.json`

**Example:**
```bash
python create_postman_collection.py
```

### `parse_canvas_markdown.py`

Standalone markdown parser for debugging and testing.

```bash
python parse_canvas_markdown.py [file_path]
```

**Arguments:**
- `file_path` (optional) - Specific markdown file to parse
- If no file specified, parses all files in `canvas_api_resources/`

**Examples:**
```bash
# Parse all files
python parse_canvas_markdown.py

# Parse specific file
python parse_canvas_markdown.py canvas_api_resources/courses.md
```

**Output:**
- Parsed endpoint information
- Parameter details
- OAuth scopes
- Debugging information

### `get_api_docs_in_markdown.py`

Canvas API documentation fetcher.

```bash
python get_api_docs_in_markdown.py [options]
```

**Options:**
- Currently no command-line options
- Downloads all available Canvas API resources
- Saves to `canvas_api_resources/` directory

**Example:**
```bash
python get_api_docs_in_markdown.py
```

### `test_collection.py`

Collection validation and testing script.

```bash
python test_collection.py [collection_file]
```

**Arguments:**
- `collection_file` (optional) - Path to collection JSON file
- Defaults to `output/canvas_api.postman_collection.json`

**Examples:**
```bash
# Test default collection
python test_collection.py

# Test specific collection file
python test_collection.py my_collection.json
```

**Output:**
- Validation results
- Collection statistics
- Error details if validation fails

## Environment Variables

### Optional Environment Variables

#### `CANVAS_API_BASE_URL`
Override the default Canvas API documentation URL.

```bash
export CANVAS_API_BASE_URL="https://canvas.instructure.com/doc/api"
python get_api_docs_in_markdown.py
```

#### `OUTPUT_DIR`
Override the default output directory.

```bash
export OUTPUT_DIR="./my_output"
python create_postman_collection.py
```

## Exit Codes

All scripts use standard exit codes:

- **0** - Success
- **1** - General error
- **2** - Invalid arguments
- **3** - File not found
- **4** - Network error (for fetching docs)
- **5** - Validation error

## Common Usage Patterns

### Full Workflow
```bash
# 1. Fetch latest documentation
just fetch-docs

# 2. Generate collection
just collection

# 3. Validate collection
just test

# 4. Import output/canvas_api.postman_collection.json into Postman
```

### Development Workflow
```bash
# Start documentation server
just docs-serve &

# Make changes to code
# ... edit files ...

# Test changes
just collection
just test

# Format documentation
just format-docs
```

### Debugging Workflow
```bash
# Parse specific file for debugging
python parse_canvas_markdown.py canvas_api_resources/courses.md

# Generate collection with verbose output
python -v create_postman_collection.py

# Validate with detailed output
python test_collection.py
```

## Troubleshooting Commands

### Check Dependencies
```bash
# Check Python version
python --version

# Check uv installation
uv --version

# Check just installation
just --version

# List installed packages
uv pip list
```

### Clean and Rebuild
```bash
# Remove generated files
rm -rf output/
rm -rf canvas_api_resources/

# Fetch fresh documentation
just fetch-docs

# Generate new collection
just collection
```

### Debug Parsing Issues
```bash
# Parse with Python verbose mode
python -v parse_canvas_markdown.py > debug.log 2>&1

# Check for specific patterns
grep -n "ERROR\|WARNING" debug.log

# Test specific regex patterns
python -c "
import re
pattern = re.compile(r'\*\*\`(GET|POST|PUT|DELETE|PATCH)\s+([^\`]+)\`\*\*')
with open('canvas_api_resources/courses.md') as f:
    content = f.read()
    matches = pattern.findall(content)
    print(f'Found {len(matches)} endpoints')
"
```
