# Notion Markdown Extractor Prototype

A standalone Python CLI tool that extracts Notion pages and converts them to Markdown files with local image downloads. Built for rapid extraction of business documentation for use with Claude Code.

## Overview

This is a **prototype** CLI tool designed for:
- Extracting individual Notion pages to clean Markdown format
- Downloading images locally with relative path references
- Converting special Notion blocks (callouts, tables, toggles) to Markdown equivalents
- Quick, reliable extraction of 20-25 business proposal documents

**Status**: In Development (Prototype Phase)

## Features

✅ Single-page extraction from Notion
✅ Local image downloads with relative paths
✅ Rich block type support (headings, lists, code, tables, callouts, toggles)
✅ UTF-8 encoding for Windows compatibility
✅ Global CLI installation for cross-project usage
✅ Clean Markdown output optimized for Claude Code

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

### 2. Install the CLI Tool Globally

```bash
cd "Software Projects/notion-markdown-extractor"
uv tool install .
```

### 3. Configure Notion API Token

```bash
notion-md configure --token <your-notion-integration-token>
```

**How to get your Notion API token:**
1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Give it a name (e.g., "Markdown Extractor")
4. Copy the "Internal Integration Token"
5. Share the Notion pages you want to extract with this integration

## Usage

### Extract a Single Page

```bash
# Extract to current directory (uses page title for filename)
notion-md extract https://www.notion.so/Your-Page-Title-abc123

# Extract to specific file
notion-md extract https://www.notion.so/Your-Page-Title-abc123 --output ~/Documents/business-proposal.md

# Extract with custom output directory
notion-md extract <notion-url> --output ./exports/my-document.md
```

### Check Configuration Status

```bash
notion-md status
```

## Output Structure

When you extract a page, the tool creates:

```
output-directory/
├── your-document.md          # Markdown file
└── images/                   # Downloaded images
    ├── diagram-1.png
    ├── chart-2.jpg
    └── screenshot-3.png
```

The Markdown file uses relative paths: `![alt text](./images/diagram-1.png)`

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
- Databases
- Embedded content
- Video/Audio
- Column layouts
- Synced blocks

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
cd "Software Projects/notion-markdown-extractor/execute"

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

### Current: Prototype (v0.1)
- ✅ Single-page extraction
- ✅ Local image downloads
- ✅ Core block types
- ✅ Global CLI installation

### Future: Enhanced Version (v2.0)
- Batch extraction from databases
- Automatic link following
- Advanced block types (databases, embeds)
- Multi-workspace support
- BMAD BMB Agent integration

## Documentation

- **PRD**: `plan/prd-notion-md-extractor-prototype-2025-10-06.md`
- **Original Project Plan**: `user-context/notion-md-cli-project-plan-2025-10-06.md`
- **Workspace Guidelines**: `../../CLAUDE.md`

## License

Internal tool for personal/business use.

## Support

For issues or questions about this prototype, refer to the PRD or project documentation in `plan/` and `user-context/` directories.

---

**Built with:** Python 3.13.7 | UV Package Manager | Click CLI Framework | Notion API

**Status**: Prototype - Fast extraction for immediate business needs
