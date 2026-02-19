# Development Guide

- **Project:** notion-markdown-extractor
- **Generated:** 2026-01-04

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.12+ | Confirmed working with 3.13.7 |
| UV Package Manager | Latest | Fast Python package management |
| Notion API Token | - | Integration token from Notion workspace |

## Installation

### 1. Install UV Package Manager

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Setup

```bash
cd notion-markdown-extractor/execute
uv sync  # Install dependencies from uv.lock
```

### 3. Install CLI Globally (Optional)

```bash
uv tool install .
```

## Development Commands

| Command | Description |
|---------|-------------|
| `uv sync` | Install/sync dependencies |
| `uv run pytest` | Run tests |
| `uv run pytest --cov` | Run tests with coverage |
| `uv run python -m notion_markdown_extractor` | Run CLI locally |

## Environment Setup

### Notion API Token

**Option 1: CLI Configuration (Recommended)**
```bash
notion-md configure --token <your-token>
# Saves to: ~/.notion-md/config.yaml
```

**Option 2: Environment Variable**
```bash
export NOTION_API_TOKEN=<your-token>
```

### Getting a Notion Token

1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Name it (e.g., "Markdown Extractor")
4. Copy the "Internal Integration Token"
5. Share target pages with the integration

## Project Structure

```
execute/
├── src/notion_markdown_extractor/  # Source code
├── tests/                          # Test suites
├── pyproject.toml                  # Project config
├── uv.lock                         # Dependency lock
└── .python-version                 # Python version
```

## Dependencies

### Runtime
- `click>=8.3.0` - CLI framework
- `notion-client>=2.5.0` - Notion API SDK
- `pillow>=11.3.0` - Image processing
- `python-dotenv>=1.1.1` - Environment loading
- `pyyaml>=6.0.3` - YAML parsing
- `requests>=2.32.5` - HTTP client

### Development
- `pytest>=8.4.2` - Test framework
- `pytest-cov>=7.0.0` - Coverage reporting
- `pytest-mock>=3.15.1` - Mocking utilities

## Testing

```bash
cd execute

# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run specific test file
uv run pytest tests/test_cli.py

# Verbose output
uv run pytest -v
```

## Building

The project uses `uv_build` as the build backend:

```bash
cd execute
uv build  # Creates dist/ with wheel and sdist
```

## Common Tasks

### Extract a Notion Page (Dev Mode)

```bash
cd execute
uv run python -m notion_markdown_extractor extract "https://notion.so/Page-abc123"
```

### Check Configuration Status

```bash
notion-md status
```

### Add a New Dependency

```bash
cd execute
uv add <package>           # Runtime dependency
uv add --dev <package>     # Dev dependency
```

## Troubleshooting

### Token Issues
- Verify token at https://www.notion.so/my-integrations
- Ensure integration has access to target pages
- Check `~/.notion-md/config.yaml` exists

### Import Errors
```bash
cd execute
uv sync  # Reinstall dependencies
```

### Windows UTF-8 Issues
```powershell
chcp 65001  # Set console to UTF-8
```
