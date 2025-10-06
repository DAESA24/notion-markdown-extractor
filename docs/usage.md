# Usage Guide

Complete reference for using the Notion Markdown Extractor CLI tool.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Extracting Pages](#extracting-pages)
- [Auto-Directory Feature](#auto-directory-feature)
- [Command Reference](#command-reference)
- [Examples](#examples)

---

## Installation

### Install Globally with UV

```bash
# Install from local repository
cd execute
uv tool install .

# Verify installation
notion-md --help
```

### Uninstall

```bash
uv tool uninstall notion-markdown-extractor
```

---

## Configuration

### First-Time Setup

Before extracting pages, you need to configure your Notion API token:

```bash
notion-md configure --token YOUR_NOTION_API_TOKEN
```

This saves your token to `~/.notion-md/config.yaml` for reuse across all commands.

**Where to get your API token**: See [Notion Setup Guide](notion-setup.md)

### Check Configuration Status

```bash
notion-md status
```

**Output**:
```
[OK] API token configured
Config file: /Users/you/.notion-md/config.yaml

Testing API connection...
[OK] API connection successful!
```

---

## Extracting Pages

### Basic Extraction

Extract a Notion page to markdown:

```bash
notion-md extract <NOTION_PAGE_URL>
```

**Example**:
```bash
notion-md extract "https://www.notion.so/My-Page-Title-abc123def456"
```

### Where Files Are Saved

The tool uses **automatic directory organization**:

#### In Project Directories (Recommended)
When you run the command from inside a **Software Projects** or **Thought Projects** directory:

```bash
cd "Thought Projects/my-research-project"
notion-md extract "https://www.notion.so/Research-Notes-abc123"

# → Saves to: ./user-context/notion-pages/research-notes.md
# → Images to: ./user-context/notion-pages/images/
```

The tool automatically:
1. Detects you're in a project directory
2. Creates `user-context/notion-pages/` if it doesn't exist
3. Saves the markdown file there with a kebab-case filename
4. Downloads images to the `images/` subdirectory

#### In Other Directories (Fallback)
When run from any other directory:

```bash
cd ~/Downloads
notion-md extract "https://www.notion.so/My-Page-abc123"

# → Still creates: ./user-context/notion-pages/my-page.md
# → You can move this directory to your project later
```

---

## Auto-Directory Feature

### How It Works

**Default Behavior (No `--output` flag)**:
1. Checks if current directory is in "Software Projects" or "Thought Projects"
2. Creates `./user-context/notion-pages/` structure
3. Saves file as `<page-title-kebab-case>.md`
4. Downloads images to `./user-context/notion-pages/images/`

**Benefits**:
- ✅ Consistent organization across all projects
- ✅ Extracted pages available as context for Claude Code
- ✅ No manual directory creation needed
- ✅ Images stay with the markdown file

### Overriding Auto-Directory

Use `--output` to specify a custom location:

```bash
notion-md extract "https://notion.so/Page-abc123" --output ~/custom/path/filename.md

# → Saves to: ~/custom/path/filename.md
# → Images to: ~/custom/path/images/
```

When you use `--output`, the auto-directory feature is disabled and your path is used exactly as specified.

---

## Command Reference

### `notion-md configure`

Configure Notion API token.

**Usage**:
```bash
notion-md configure --token <YOUR_TOKEN>
```

**Options**:
- `--token` (required): Your Notion integration token

**Example**:
```bash
notion-md configure --token secret_abc123xyz789
```

---

### `notion-md status`

Check configuration and API connectivity.

**Usage**:
```bash
notion-md status
```

**Output**:
- Token configuration status
- Config file location
- API connection test result

---

### `notion-md extract`

Extract a Notion page to Markdown.

**Usage**:
```bash
notion-md extract <PAGE_URL> [OPTIONS]
```

**Arguments**:
- `PAGE_URL` (required): Full URL of the Notion page to extract

**Options**:
- `--output`, `-o`: Custom output file path (overrides auto-directory)

**Examples**:

```bash
# Auto-directory (default)
notion-md extract "https://notion.so/My-Page-abc123"

# Custom output file
notion-md extract "https://notion.so/My-Page-abc123" --output notes.md

# Custom output with full path
notion-md extract "https://notion.so/My-Page-abc123" --output ~/Documents/research/notes.md

# Short flag syntax
notion-md extract "https://notion.so/My-Page-abc123" -o output.md
```

---

## Examples

### Thought Project Workflow

```bash
# Navigate to your thought project
cd "Thought Projects/virgo-capital-sor-opportunity"

# Extract multiple Notion pages
notion-md extract "https://notion.so/Framework-Page-abc123"
notion-md extract "https://notion.so/Research-Notes-def456"
notion-md extract "https://notion.so/Meeting-Notes-ghi789"

# All saved to: ./user-context/notion-pages/
# ├── framework-page.md
# ├── research-notes.md
# ├── meeting-notes.md
# └── images/
#     ├── diagram1.png
#     ├── chart2.png
#     └── ...
```

### Software Project Workflow

```bash
# Navigate to your software project
cd "Software Projects/my-app"

# Extract design docs
notion-md extract "https://notion.so/Architecture-Design-abc123"
notion-md extract "https://notion.so/API-Specification-def456"

# All saved to: ./user-context/notion-pages/
# Available as context when working with Claude Code
```

### Custom Output Locations

```bash
# Extract to project docs folder
notion-md extract "https://notion.so/User-Guide-abc123" --output docs/user-guide.md

# Extract to specific directory with custom name
notion-md extract "https://notion.so/Q4-Report-abc123" --output ~/reports/2024-q4-analysis.md

# Extract to current directory
notion-md extract "https://notion.so/Quick-Note-abc123" --output ./quick-note.md
```

### Batch Extraction Script

Create a shell script to extract multiple pages:

```bash
#!/bin/bash
# extract-project-docs.sh

cd "Thought Projects/my-project"

# Array of Notion URLs
PAGES=(
  "https://notion.so/Overview-abc123"
  "https://notion.so/Strategy-def456"
  "https://notion.so/Timeline-ghi789"
)

# Extract all pages
for page in "${PAGES[@]}"; do
  notion-md extract "$page"
done

echo "All pages extracted to ./user-context/notion-pages/"
```

---

## Output Format

### File Structure

**Markdown file**:
- Page title as H1 heading
- All content converted to GitHub-flavored markdown
- Rich text formatting preserved (bold, italic, links)
- Code blocks with syntax highlighting
- Images with relative path references

**Images directory**:
- Downloaded images with sanitized filenames
- Relative paths in markdown: `![alt](./images/image-name.png)`

### Example Output

**Directory structure**:
```
user-context/notion-pages/
├── my-project-overview.md
├── technical-architecture.md
└── images/
    ├── architecture-diagram.png
    ├── user-flow-chart.png
    └── screenshot-dashboard.jpg
```

**Markdown content**:
```markdown
# My Project Overview

This is a **bold** statement with *italic* emphasis.

## Section Heading

- Bulleted list item 1
- Bulleted list item 2

### Code Example

```python
def hello_world():
    print("Hello, world!")
```

### Diagram

![Architecture Diagram](./images/architecture-diagram.png)
```

---

## Supported Features

### Block Types

**Fully Supported**:
- ✅ Headings (H1, H2, H3)
- ✅ Paragraphs
- ✅ Bulleted lists
- ✅ Numbered lists
- ✅ Code blocks (with syntax highlighting)
- ✅ Quotes
- ✅ Callouts (converted to blockquotes)
- ✅ Toggles (flattened to headings)
- ✅ Images (downloaded locally)
- ✅ Files (download links)
- ✅ Tables
- ✅ Dividers
- ✅ Synced blocks (reusable content)
- ✅ Child page references (as links)

**Not Yet Supported** (Phase 2):
- ❌ Column layouts (flattened)
- ❌ Databases (shows warning)
- ❌ Embeds (videos, etc.)
- ❌ Advanced formatting

### Rich Text

**Supported Annotations**:
- ✅ Bold (`**text**`)
- ✅ Italic (`*text*`)
- ✅ Inline code (`` `text` ``)
- ✅ Links (`[text](url)`)
- ✅ Strikethrough (`~~text~~`)

---

## Troubleshooting

### "No API token configured"

**Solution**: Run `notion-md configure --token YOUR_TOKEN` first

### "Failed to fetch page"

**Causes**:
1. Page not shared with integration → See [Notion Setup Guide](notion-setup.md)
2. Invalid URL or page ID
3. Network connectivity issues

**Solution**: Verify page sharing in Notion

### Missing Content

**Causes**:
1. Child pages not shared → Share all linked pages
2. Synced block sources not shared → Share source pages
3. Unsupported block types → Check warnings

**Solution**: See [Notion Setup Guide](notion-setup.md#sharing-pages) for sharing requirements

### Images Not Downloading

**Causes**:
1. Image URLs expired (Notion URLs are temporary)
2. Network issues
3. Permission problems

**Solution**: Check extraction output for `[WARNING] Failed to download image` messages

---

## Tips & Best Practices

### 1. Organize in Project Directories
Always run from your Software Projects or Thought Projects directory to use auto-organization.

### 2. Share All Related Pages
Before extraction, share:
- Main page
- All child/linked pages
- Synced block source pages

Use Notion's "Include sub-pages" checkbox when sharing.

### 3. Handle Unsupported Blocks
If you see warnings about unsupported blocks:
- Content won't be lost, just won't render
- Check the original Notion page for that content
- Phase 2 will add support

### 4. Batch Extract Multiple Pages
Create a script to extract all your project pages at once.

### 5. Use Relative Paths
Extracted files use relative image paths, so you can move the entire `notion-pages/` directory and links still work.

---

## Environment Variables

### `NOTION_API_TOKEN`

Alternative to using `notion-md configure`:

```bash
export NOTION_API_TOKEN="secret_abc123xyz"
notion-md extract "https://notion.so/Page-abc123"
```

Token priority:
1. Environment variable `NOTION_API_TOKEN` (checked first)
2. Config file `~/.notion-md/config.yaml` (fallback)

---

## Getting Help

```bash
# Show all commands
notion-md --help

# Show help for specific command
notion-md extract --help
notion-md configure --help
notion-md status --help

# Show version
notion-md --version
```

---

## Next Steps

- [Notion Setup Guide](notion-setup.md) - Configure your Notion integration
- [Troubleshooting Guide](troubleshooting.md) - Common issues and solutions
- [Feature Reference](features.md) - Detailed block type support
