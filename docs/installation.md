# Installation

## Prerequisites

- **Python ≥3.13** (recommended) or Python ≥3.10 (minimum)
- **Git** for cloning the repository
- **uv** (recommended) or **pip** for dependency management

## Installing uv (Recommended)

uv is a fast Python package installer and resolver. Install it using:

=== "macOS/Linux"
`bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    `

=== "Windows"
`powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    `

=== "pip"
`bash
    pip install uv
    `

## Installation Methods

### Method 1: Using uv (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd canvas-api-postman-master

# Create virtual environment and install dependencies
uv venv
uv pip install -e .

# Activate virtual environment (if needed)
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

### Method 2: Using pip

```bash
# Clone the repository
git clone <repository-url>
cd canvas-api-postman-master

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

### Method 3: Development Installation

For development work, install with documentation dependencies:

```bash
# Using uv
uv pip install -e ".[dev]"

# Using pip
pip install -e ".[dev]"
```

## Verify Installation

Test that everything is working:

```bash
# Check Python version
python --version

# Test the collection generator
python create_postman_collection.py --help

# Run validation tests
python test_collection.py
```

## Dependencies

The project uses these main dependencies:

### Core Dependencies

- **requests** ≥2.32.5 - HTTP library for API calls
- **beautifulsoup4** ≥4.12.0 - HTML/XML parsing
- **markdown** ≥3.7 - Markdown processing
- **python-frontmatter** ≥1.1.0 - YAML frontmatter parsing

### Development Dependencies

- **mkdocs-material** ≥9.5.0 - Documentation generator
- **mkdocstrings[python]** ≥0.24.0 - API documentation

## Troubleshooting

### Common Issues

**Python Version Error**

```
ERROR: This package requires Python >=3.10
```

**Solution**: Upgrade Python or use pyenv/conda to manage Python versions.

**uv Not Found**

```
command not found: uv
```

**Solution**: Install uv using the installation script above, or use pip instead.

**Permission Errors**

```
PermissionError: [Errno 13] Permission denied
```

**Solution**: Use virtual environments or install with `--user` flag.

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/your-org/canvas-api-postman/issues)
2. Verify your Python version: `python --version`
3. Check virtual environment activation
4. Try reinstalling dependencies: `uv pip install --force-reinstall -e .`

## Next Steps

After installation, proceed to the [Usage Guide](usage.md) to generate your first Postman collection.
