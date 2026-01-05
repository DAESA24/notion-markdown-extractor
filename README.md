# Notion Markdown Extractor

A Python CLI tool that extracts Notion pages and converts them to Markdown files with automatic project organization. Built for seamless integration with Claude Code workflows.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Output Structure](#output-structure)
- [Supported Notion Block Types](#supported-notion-block-types)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Uninstalling](#uninstalling)
- [Roadmap](#roadmap)
- [Documentation](#documentation)
- [Credits](#credits)

## Overview

Extract Notion pages to clean Markdown format with automatic organization into your project structure:
- **Auto-directory creation**: Saves to `user-context/notion-pages/` in your projects
- **Local image downloads**: All images downloaded with relative path references
- **Rich block support**: Converts callouts, tables, toggles, synced blocks, and more
- **Project-aware**: Works from any project directory
- **Cross-project usage**: Global CLI installation works from any directory

**Status**: MVP Complete ✅

## Features

✅ **Auto-organizing extractions** - Saves to `user-context/notion-pages/` automatically
✅ **Project detection** - Auto-organizes in any project directory
✅ **Synced block support** - Extracts reusable Notion content correctly
✅ **Local image downloads** - All images saved with relative paths
✅ **Rich block types** - Headings, lists, code, tables, callouts, toggles, and more
✅ **UTF-8 encoding** - Windows-compatible out of the box
✅ **Global CLI** - Use from any directory
✅ **Clean Markdown** - Optimized for Claude Code context

## Requirements

- **Python**: 3.12+ (confirmed working with 3.13.7)
- **UV Package Manager**: Fast Python package manager
- **Notion API Token**: Integration token from Notion workspace

## Installation

### 1. Install UV Package Manager

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository

```bash
git clone https://github.com/DAESA24/notion-markdown-extractor.git
```

### 3. Install the CLI Tool Globally

```bash
cd notion-markdown-extractor/execute
uv tool install .
```

### 4. Configure Notion API Token

```bash
notion-md configure --token <your-notion-integration-token>
```

**How to get your Notion API token:**
1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Give it a name (e.g., "Markdown Extractor")
4. Copy the "Internal Integration Token"
5. Share the Notion pages you want to extract with this integration

## Quick Start

### Basic Usage (Auto-organizing)

```bash
# Navigate to your project
cd my-research-project

# Extract a Notion page (auto-saves to user-context/notion-pages/)
notion-md extract "https://www.notion.so/Your-Page-Title-abc123"

# ✅ Saved to: ./user-context/notion-pages/your-page-title.md
# ✅ Images to: ./user-context/notion-pages/images/
```

### Custom Output Location

```bash
# Override auto-directory with explicit path
notion-md extract "https://notion.so/Page-abc123" --output ~/Documents/notes.md
```

### Check Configuration

```bash
notion-md status
```

## Output Structure

**Auto-organized** (default in projects):
```
user-context/notion-pages/
├── framework-document.md
├── meeting-notes.md
├── strategic-plan.md
└── images/
    ├── architecture-diagram.png
    ├── workflow-chart.png
    └── screenshot.jpg
```

**Custom location** (with `--output` flag):
```
your-custom-path/
├── custom-name.md
└── images/
    └── downloaded-images.png
```

## Supported Notion Block Types

### Fully Supported (MVP)
- **Text**: Paragraphs, Headings (1-3), Quotes
- **Lists**: Bulleted, Numbered (with nesting)
- **Code**: Code blocks with syntax highlighting, Inline code
- **Media**: Images (downloaded locally), File attachments
- **Structure**: Dividers, Tables, Callouts, Toggle blocks
- **Links**: Internal page references (converted to placeholders)

### Conversion Examples

**Callouts** → Blockquotes with emoji:
```markdown
> 💡 **Key Point** This is important information
```

**Toggle Blocks** → Flattened to headings:
```markdown
### Section Title
Content that was inside the toggle
```

**Tables** → Markdown tables:
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

**Internal Links** → Placeholders:
```markdown
[Related Document Name - see separate import]
```

### Deferred to Future Versions
- Databases (inline and full-page)
- Embedded content
- Video/Audio
- Column layouts (content extracted but layout flattened)

## Development

### Project Structure

```
notion-markdown-extractor/
├── explore/           # Research and discovery
├── plan/              # Planning documents (PRD)
├── execute/           # Implementation
│   ├── src/          # Python source code
│   ├── tests/        # Test suites
│   └── pyproject.toml
├── user-context/      # Context files
└── README.md          # This file
```

### Development Setup

```bash
# Navigate to project
cd notion-markdown-extractor/execute

# Install dependencies
uv add click notion-client python-dotenv requests Pillow
uv add --dev pytest pytest-mock pytest-cov

# Run tests
uv run pytest

# Run CLI locally (development mode)
uv run python -m src.cli extract <notion-url>
```

## Troubleshooting

### "Token invalid or expired"
- Verify your token in Notion settings
- Ensure the integration has access to the page you're trying to extract
- Re-run `notion-md configure --token <new-token>`

### "Page not found"
- Check that the Notion page URL is correct
- Ensure the integration is shared with the page (click Share → Add integration)

### "Image download failed"
- Tool will log the error and continue processing
- Check network connection
- Verify images are accessible (not private external images)

### UTF-8 Encoding Issues on Windows
- Tool automatically handles UTF-8 encoding
- If issues persist, check terminal encoding: `chcp 65001`

## Uninstalling

```bash
# Remove global CLI tool
uv tool uninstall notion-markdown-extractor

# Remove configuration
rm -rf ~/.notion-md/
```

## Roadmap

### MVP Complete

- ✅ Single-page extraction
- ✅ Local image downloads
- ✅ Core block types
- ✅ Global CLI installation

### Future: Enhanced Version

- Batch extraction from databases
- Automatic link following
- Advanced block types (databases, embeds)
- Multi-workspace support
- BMAD BMB Agent integration

## Documentation

### User Documentation

- **[Usage Guide](docs/user-docs/usage.md)** - Complete CLI reference and examples
- **[Notion Setup Guide](docs/user-docs/notion-setup.md)** - Integration setup and permissions

### Project Documentation

- **[PRD](docs/project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md)** - Product requirements
- **[Architecture](docs/architecture.md)** - System architecture and design decisions

## Credits

This project was developed using the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) - an AI-driven agile development framework for building software with AI agents.

## License

Internal tool for personal/business use.

## Support

For issues or questions, refer to the PRD or project documentation in the `docs/` directory.

---

**Built with:** Python 3.13.7 | UV Package Manager | Click CLI Framework | Notion API

**Status**: MVP Complete
