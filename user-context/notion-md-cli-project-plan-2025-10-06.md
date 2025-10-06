# Notion Markdown Extractor - CLI Tool Project Plan

## Context for Claude Code

This document captures the project plan for building a standalone Python CLI tool that extracts Notion pages in block format and converts them to Markdown files. This tool is needed **immediately** for a business proposal project.

## Background Discussion Summary

### User's Immediate Need
- Extract Notion pages in block format → Markdown
- Use converted files with Claude Code for business proposal work
- Need working tool quickly (2-3 hours build time target)

### Why This Approach (Not BMAD v6-alpha BMB)
1. **Speed**: Direct Python tool is fastest path to working solution
2. **Stability**: v6-alpha is unstable with daily changes
3. **Proven Pattern**: Successfully used for GitIngest agent project
4. **Future-Proof**: Can add BMAD BMB agent wrapper later if desired

### Related Research Context
- User researched BMAD v6-alpha BMB (BMAD Builder) module
- BMB has `create-agent` workflow for building custom agents
- Three agent types: Simple, Expert (with sidecar resources), Module
- Expert Agent would be ideal **later** for wrapping this CLI tool
- For now: Build working CLI first, agent integration second

## Project Structure

```
notion-markdown-extractor/
├── user-context/                    # Project planning and context
│   └── notion-md-cli-project-plan-2025-10-06.md  # This file
├── cli.py                           # Click-based CLI framework
├── notion_client.py                 # Notion API wrapper
├── block_converter.py               # Block → Markdown conversion logic
├── storage.py                       # File saving and path management
├── config.py                        # API token configuration
├── pyproject.toml                   # UV project configuration
├── README.md                        # Installation and usage guide
└── tests/                           # Test suite (pytest)
    ├── test_cli.py
    ├── test_notion_client.py
    ├── test_block_converter.py
    └── test_storage.py
```

## Implementation Plan

### Task 1: Research Notion API and Block Format Extraction
**Goal**: Understand Notion API authentication, block types, and extraction patterns

**Key Questions to Answer**:
- How to authenticate with Notion API (integration token)
- How to retrieve page content (pages vs blocks endpoints)
- What block types exist (paragraph, heading, list, code, etc.)
- How nested blocks are structured
- Rate limiting and pagination considerations

**Research Resources**:
- Notion API Documentation: https://developers.notion.com/
- Official Python SDK: `notion-client` package
- Block types reference: https://developers.notion.com/reference/block

**Deliverables**:
- List of Notion block types to support
- Authentication flow design
- API endpoint usage patterns

---

### Task 2: Design CLI Structure
**Goal**: Define CLI commands, arguments, and user workflow

**Core Commands**:

```bash
# One-time configuration
notion-md configure --token <notion-integration-token>

# Extract single page
notion-md extract <notion-page-url> --output <output-file.md>

# Batch extract from database/workspace
notion-md batch-extract <database-url> --output-dir <directory>

# Show configuration status
notion-md status
```

**CLI Design Pattern** (following GitIngest agent pattern):
- Use `click` for CLI framework
- Support both positional and named arguments
- Clear error messages with actionable suggestions
- Progress indicators for long operations
- UTF-8 encoding support (lessons learned from GitIngest)

**Deliverables**:
- CLI command specification
- Help text for each command
- Error handling strategy

---

### Task 3: Implement Notion API Authentication and Page Fetching
**Goal**: Build `notion_client.py` module for API interactions

**Core Functions Needed**:

```python
class NotionClient:
    def __init__(self, token: str):
        """Initialize with Notion integration token"""

    def get_page(self, page_id: str) -> dict:
        """Fetch page metadata and properties"""

    def get_blocks(self, block_id: str, recursive: bool = True) -> list:
        """Fetch all blocks for a page (with children)"""

    def get_database_pages(self, database_id: str) -> list:
        """Fetch all pages from a database"""
```

**Technical Considerations**:
- Store token securely (environment variable or config file)
- Handle pagination for large pages (100 blocks per request limit)
- Recursive block fetching for nested content
- Error handling for invalid tokens, missing pages, permissions

**Deliverables**:
- Working `notion_client.py` module
- Token configuration management
- Robust error handling

---

### Task 4: Implement Block-to-Markdown Conversion Logic
**Goal**: Build `block_converter.py` module to transform Notion blocks → Markdown

**Notion Block Types to Support** (priority order):

1. **Text Blocks**:
   - Paragraph
   - Heading 1, 2, 3
   - Bulleted list
   - Numbered list
   - Quote
   - Callout

2. **Code & Technical**:
   - Code block (with language syntax)
   - Inline code

3. **Media**:
   - Image (download or reference URL)
   - File attachments

4. **Structural**:
   - Divider (horizontal rule)
   - Table of contents
   - Toggle blocks
   - Child page references

**Conversion Functions**:

```python
def convert_block_to_markdown(block: dict) -> str:
    """Convert single Notion block to Markdown"""

def convert_blocks_to_markdown(blocks: list) -> str:
    """Convert list of blocks to complete Markdown document"""

def handle_nested_blocks(block: dict, indent_level: int = 0) -> str:
    """Handle blocks with children (lists, toggles)"""
```

**Technical Considerations**:
- Preserve rich text annotations (bold, italic, code, links)
- Handle nested blocks (indentation for lists)
- Escape special Markdown characters where needed
- Maintain proper spacing between blocks

**Deliverables**:
- Working block-to-Markdown converter
- Support for all priority block types
- Clean, readable Markdown output

---

### Task 5: Add Storage and File Management
**Goal**: Build `storage.py` module for saving converted Markdown files

**Core Functions**:

```python
def save_markdown(content: str, output_path: str) -> str:
    """Save Markdown content to file with UTF-8 encoding"""

def ensure_directory(path: str) -> Path:
    """Create directory if it doesn't exist"""

def sanitize_filename(title: str) -> str:
    """Convert page title to safe filename (kebab-case)"""

def get_output_path(page_title: str, output_dir: str) -> str:
    """Generate output path from page title"""
```

**Technical Considerations**:
- UTF-8 encoding (lessons from GitIngest encoding issues)
- Handle Windows path restrictions
- Generate safe filenames from page titles
- Create output directories automatically
- Handle file overwrite conflicts

**Deliverables**:
- Working storage module
- Safe filename generation
- Directory management

---

### Task 6: Integrate CLI Commands with Click Framework
**Goal**: Build `cli.py` with all commands using Click decorators

**CLI Structure**:

```python
import click
from notion_client import NotionClient
from block_converter import convert_blocks_to_markdown
from storage import save_markdown, get_output_path

@click.group()
def notion_md():
    """Notion Markdown Extractor - Convert Notion pages to Markdown"""
    pass

@notion_md.command()
@click.option('--token', required=True, help='Notion integration token')
def configure(token: str):
    """Configure Notion API authentication"""
    # Save token to config file

@notion_md.command()
@click.argument('page_url')
@click.option('--output', default=None, help='Output file path')
def extract(page_url: str, output: str):
    """Extract single Notion page to Markdown"""
    # 1. Parse page ID from URL
    # 2. Fetch page content via NotionClient
    # 3. Convert blocks to Markdown
    # 4. Save to file

@notion_md.command()
@click.argument('database_url')
@click.option('--output-dir', default='./notion-exports', help='Output directory')
def batch_extract(database_url: str, output_dir: str):
    """Batch extract pages from Notion database"""
    # 1. Parse database ID from URL
    # 2. Fetch all pages in database
    # 3. Extract each page
    # 4. Save with sanitized filenames

@notion_md.command()
def status():
    """Show configuration status and connection test"""
    # Display configured token status
    # Test Notion API connection
```

**pyproject.toml Configuration**:

```toml
[project]
name = "notion-markdown-extractor"
version = "0.1.0"
description = "Extract Notion pages and convert to Markdown"
requires-python = ">=3.12"
dependencies = [
    "click>=8.1.0",
    "notion-client>=2.2.0",
    "python-dotenv>=1.0.0",
]

[project.scripts]
notion-md = "cli:notion_md"
```

**Deliverables**:
- Complete CLI with all commands
- Entry point configuration
- Working `uv run notion-md` execution

---

### Task 7: Testing and Validation
**Goal**: Test with user's actual Notion pages for business proposal

**Test Plan**:

1. **Configuration Test**:
   - Run `notion-md configure --token <token>`
   - Verify token saved correctly
   - Test `notion-md status`

2. **Single Page Extraction**:
   - Extract one simple page (mostly text)
   - Verify Markdown output quality
   - Check UTF-8 encoding handling

3. **Complex Page Test**:
   - Extract page with headings, lists, code blocks
   - Verify nested block handling
   - Check formatting preservation

4. **Batch Extraction** (if needed):
   - Extract multiple pages from database
   - Verify filename generation
   - Check directory creation

5. **Edge Cases**:
   - Empty pages
   - Pages with special characters in title
   - Pages with unsupported block types
   - Permission errors

**Deliverables**:
- Working tool tested on user's Notion pages
- Markdown files ready for Claude Code business proposal work
- Known limitations documented

---

## Technology Stack

### Core Dependencies
- **Python 3.12+**: Language
- **UV**: Package manager (fast, proven with GitIngest agent)
- **Click**: CLI framework (same as GitIngest agent)
- **notion-client**: Official Notion Python SDK
- **python-dotenv**: Environment variable management

### Development Dependencies
- **pytest**: Testing framework
- **pytest-mock**: Mocking for tests
- **pytest-cov**: Code coverage

## Installation Steps

### For Development:

```bash
cd "Software Projects/notion-markdown-extractor"

# Initialize UV project (if not already done)
uv init

# Add dependencies
uv add click notion-client python-dotenv
uv add --dev pytest pytest-mock pytest-cov

# Run CLI
uv run notion-md --help
```

### For User:

```bash
# Configure once
uv run notion-md configure --token <notion-integration-token>

# Extract pages
uv run notion-md extract <notion-page-url> --output business-proposal.md
```

## Configuration Management

### Token Storage Options:

**Option 1: Config File** (Recommended)
```
~/.notion-md/config.yaml
```

**Option 2: Environment Variable**
```
NOTION_API_TOKEN=secret_xxxx
```

**Option 3: Pass with each command**
```bash
notion-md extract <url> --token <token>
```

## Known Challenges (from GitIngest Agent Experience)

### 1. UTF-8 Encoding on Windows
**Lesson Learned**: Windows uses cp1252 by default, causing Unicode errors

**Solution**:
- Always use `encoding='utf-8'` in file operations
- Use `errors='replace'` for subprocess calls
- Test with special characters in Notion content

### 2. API Rate Limiting
**Challenge**: Notion API has rate limits

**Solution**:
- Implement exponential backoff
- Add progress indicators for batch operations
- Cache page content locally

### 3. Nested Block Complexity
**Challenge**: Notion blocks can be deeply nested

**Solution**:
- Recursive block fetching
- Track indentation levels
- Handle circular references (if any)

## Future Enhancements (Post-MVP)

### Phase 2: BMAD BMB Agent Integration
- Create Expert Agent wrapper using v6-alpha BMB
- Agent commands: `*extract-page`, `*batch-extract`, `*configure`
- Sidecar resources: memories.md, session tracking
- IDE integration (Claude Code, Cursor)

### Phase 3: Advanced Features
- Watch mode (auto-sync Notion changes)
- Bi-directional sync (Markdown → Notion)
- Custom block type plugins
- Rich media handling (download images locally)

## Success Criteria

**MVP Complete When**:
1. ✅ User can configure Notion API token
2. ✅ User can extract single Notion page to Markdown
3. ✅ Markdown output is clean and usable with Claude Code
4. ✅ UTF-8 encoding works correctly on Windows
5. ✅ All priority block types convert properly
6. ✅ Tool works reliably for business proposal extraction

## Timeline Estimate

- **Task 1 (Research)**: 30 minutes
- **Task 2 (Design)**: 15 minutes
- **Task 3 (API Client)**: 45 minutes
- **Task 4 (Conversion)**: 60 minutes
- **Task 5 (Storage)**: 30 minutes
- **Task 6 (CLI Integration)**: 30 minutes
- **Task 7 (Testing)**: 30 minutes

**Total**: ~3.5 hours to working tool

## Next Steps for Claude Code

1. **Verify project structure exists** in `notion-markdown-extractor/`
2. **Start with Task 1** (Research Notion API)
3. **Follow GitIngest agent patterns** for CLI structure
4. **Test frequently** with user's actual Notion pages
5. **Prioritize working tool** over perfect code
6. **Document limitations** clearly for user

## Reference Projects

- **GitIngest Agent**: `Software Projects/gitingest-agent-project/`
  - Similar CLI structure with Click
  - UV package management patterns
  - UTF-8 encoding solutions
  - Error handling examples

## User's Primary Goal

**Get Notion pages converted to Markdown TODAY** so work can proceed on business proposal project with Claude Code.

Speed and functionality > perfection.

---

*This plan was created based on discussion with user on 2025-10-06 about building Notion Markdown Extractor CLI tool vs BMAD v6-alpha BMB agent approach.*
