# Product Requirements Document: Notion Markdown Extractor Prototype

## Executive Summary

This PRD defines requirements for building a standalone Python CLI tool that extracts Notion pages and converts them to Markdown files. This is a **prototype** focused on rapid delivery to support immediate business proposal work.

## Business Context

### Immediate Need
- Extract 20-25 specific Notion pages to Markdown format
- Use converted files with Claude Code for business proposal development
- Working tool needed urgently (target: 2-3 hours build time)

### Strategic Context
- **Current Phase**: Rapid prototype for immediate extraction needs
- **Future Phase**: More mature CLI agent with BMAD BMB integration
- **Approach**: Build working tool quickly, learn from usage, iterate later

### Why This Approach
1. **Speed**: Direct Python CLI is fastest path to working solution
2. **Disposable**: Treated as prototype that can be replaced/upgraded later
3. **Learning**: Real-world usage will inform better v2 design
4. **Proven Pattern**: Follows successful GitIngest agent project patterns

## Product Requirements

### Functional Requirements

#### FR1: API Authentication ✅ COMPLETE
- **Requirement**: Configure and store Notion API integration token
- **Priority**: P0 (Critical)
- **Acceptance Criteria**:
  - User can provide Notion API token via command
  - Token stored securely for reuse
  - Configuration status visible to user

#### FR2: Single Page Extraction ✅ COMPLETE
- **Requirement**: Extract individual Notion page to Markdown file
- **Priority**: P0 (Critical)
- **Acceptance Criteria**:
  - Accept Notion page URL as input
  - Fetch page content via Notion API
  - Convert blocks to Markdown format
  - Save to specified output file path
  - UTF-8 encoding on Windows

#### FR3: Block Type Support ✅ COMPLETE
- **Requirement**: Convert priority Notion block types to Markdown
- **Priority**: P0 (Critical)
- **Block Types** (priority order):
  1. **Text Blocks**: Paragraph, Heading 1/2/3, Bulleted list, Numbered list, Quote, Callout
  2. **Code & Technical**: Code block (with language), Inline code
  3. **Media**: Image (download locally and reference), File attachments
  4. **Structural**: Divider, Table (basic support), Toggle blocks, Child page references
- **Acceptance Criteria**:
  - All priority text blocks convert correctly
  - Rich text annotations preserved (bold, italic, links)
  - Nested blocks handle indentation
  - Code blocks include language syntax
  - Images downloaded to local directory and referenced in Markdown
  - Tables converted to Markdown table format
  - Callouts converted to blockquotes with emoji
  - Toggle blocks flattened to regular text with headings
  - Internal page links converted to placeholder text with document name

#### FR4: Global CLI Tool ✅ COMPLETE
- **Requirement**: Install CLI tool globally for use from any directory
- **Priority**: P0 (Critical)
- **Acceptance Criteria**:
  - Installable via `uv tool install`
  - Command `notion-md` works from any directory
  - Easy to uninstall/replace when upgrading to v2

### Non-Functional Requirements

#### NFR1: Performance
- Time to extract single page: < 10 seconds
- Handle pages with 100+ blocks

#### NFR2: Reliability
- Graceful error handling for API failures
- Clear error messages with actionable guidance
- Handle network timeouts and rate limits

#### NFR3: Usability
- Simple command structure (minimal required arguments)
- Progress indicators for operations
- Help text for all commands

#### NFR4: Compatibility
- Windows 11 environment
- Python 3.12+ (confirmed: 3.13.7 available)
- UTF-8 encoding support

#### FR5: Image Download and Management ✅ COMPLETE
- **Requirement**: Download images from Notion and save locally
- **Priority**: P0 (Critical)
- **Acceptance Criteria**:
  - Images downloaded to `images/` subdirectory relative to output file
  - Image filenames sanitized (kebab-case based on image metadata or hash)
  - Markdown uses relative paths to reference local images
  - Handle image download failures gracefully (log error, skip image, continue)
  - Support common image formats (PNG, JPG, GIF, WebP)

### Implemented Beyond MVP Scope

The following features were implemented during MVP development but were not in the original requirements:

#### Synced Block Support

- **Implementation**: Full support for Notion's synced/reusable content blocks
- **Behavior**: Both source and reference synced blocks are rendered with their content
- **Location**: `block_converter.py` - `_convert_synced_block()` method
- **Note**: Content appears inline where synced blocks are placed (matches Notion's display behavior)

#### Auto-Directory Organization

- **Implementation**: Automatic output to `user-context/notion-pages/` when run from project directories
- **Behavior**: Detects project context and organizes extracted pages into consistent location
- **Location**: `storage.py` - `get_auto_output_path()`, `project_detector.py`
- **Note**: Can be overridden with explicit `--output` flag

#### Rate Limiting with Exponential Backoff

- **Implementation**: Automatic retry with exponential backoff for API rate limits (429 errors)
- **Behavior**: Retries up to 3 times with 1s, 2s, 4s delays
- **Location**: `notion_client.py` - `_fetch_blocks_with_retry()` method
- **Note**: Prevents failures during extraction of large pages

---

### Out of Scope (Deferred to Phase 2)

#### Explicitly Excluded from MVP:
- **Batch extraction** from Notion databases
- **Automatic link following** (extract linked pages automatically)
- **Watch mode** (auto-sync changes)
- **Bi-directional sync** (Markdown → Notion)
- **BMAD BMB agent wrapper**
- **Advanced block types** (databases, embedded content, column layouts, synced blocks, etc.)

## Technical Specifications

### System Architecture

```
notion-markdown-extractor/
├── explore/                       # Research and discovery work
├── plan/                          # Planning documents (this PRD)
├── execute/                       # Implementation phase
│   ├── src/                      # Python CLI source code
│   │   ├── cli.py               # Click-based CLI framework
│   │   ├── notion_client.py     # Notion API wrapper
│   │   ├── block_converter.py   # Block → Markdown conversion
│   │   ├── storage.py           # File saving and path management
│   │   └── config.py            # API token configuration
│   ├── tests/                    # Test suites
│   │   ├── test_cli.py
│   │   ├── test_notion_client.py
│   │   ├── test_block_converter.py
│   │   └── test_storage.py
│   └── pyproject.toml            # UV project configuration
├── user-context/                  # Project planning documents
└── README.md
```

### Technology Stack

#### Core Dependencies
- **Python 3.13.7**: Language runtime
- **UV**: Package manager (fast, proven with GitIngest agent)
- **Click**: CLI framework
- **notion-client**: Official Notion Python SDK
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for image downloads
- **Pillow**: Image processing (validation, format handling)

#### Development Dependencies
- **pytest**: Testing framework
- **pytest-mock**: Mocking for tests
- **pytest-cov**: Code coverage

### CLI Command Structure

#### Primary Commands

```bash
# One-time configuration
notion-md configure --token <notion-integration-token>

# Extract single page
notion-md extract <notion-page-url> --output <output-file.md>

# Show configuration status
notion-md status
```

#### Command Details

**`configure`**
- Purpose: Store Notion API token for reuse
- Arguments: `--token` (required)
- Storage: Config file in `~/.notion-md/config.yaml`

**`extract`**
- Purpose: Extract single Notion page to Markdown
- Arguments:
  - `page_url` (positional, required)
  - `--output` (optional, defaults to page title in current directory)
- Process:
  1. Parse page ID from URL
  2. Fetch page content via Notion API
  3. Convert blocks to Markdown
  4. Save to file with UTF-8 encoding

**`status`**
- Purpose: Verify configuration and API connectivity
- Arguments: None
- Output: Token status, API connection test result

### API Integration

#### Notion API Endpoints
- **Authentication**: Integration token (user already has this)
- **Pages API**: Retrieve page metadata and properties
- **Blocks API**: Retrieve page content blocks (with children)

#### Key Integration Points

**NotionClient Class:**
```python
class NotionClient:
    def __init__(self, token: str):
        """Initialize with Notion integration token"""

    def get_page(self, page_id: str) -> dict:
        """Fetch page metadata and properties"""

    def get_blocks(self, block_id: str, recursive: bool = True) -> list:
        """Fetch all blocks for a page (with children)"""
```

**Technical Considerations:**
- Handle pagination (100 blocks per request limit)
- Recursive block fetching for nested content
- Rate limiting with exponential backoff
- Error handling for invalid tokens, missing pages, permissions
- Notion page properties/metadata extraction and formatting
- Handle image URLs from Notion API (both uploaded and embedded images)

### Block Conversion Logic

#### Converter Architecture

**BlockConverter Module:**
```python
def convert_block_to_markdown(block: dict) -> str:
    """Convert single Notion block to Markdown"""

def convert_blocks_to_markdown(blocks: list) -> str:
    """Convert list of blocks to complete Markdown document"""

def handle_nested_blocks(block: dict, indent_level: int = 0) -> str:
    """Handle blocks with children (lists, toggles)"""
```

**Conversion Rules:**
- Preserve rich text annotations (bold: `**text**`, italic: `*text*`, code: `` `text` ``)
- Handle nested blocks with proper indentation
- Escape special Markdown characters where needed
- Maintain proper spacing between blocks
- Code blocks include language syntax markers
- **Callouts**: Convert to blockquotes with emoji (e.g., `> 💡 **Key Point** content`)
- **Toggle blocks**: Flatten to regular text with heading level based on context
- **Tables**: Convert to Markdown table format with proper alignment
- **Internal page links**: Convert to placeholder text including document name (e.g., `[Document Name - see separate import]`)
- **Images**: Download locally and reference with relative paths (e.g., `![alt text](./images/image-name.png)`)

### File Storage

#### Storage Module

**Core Functions:**
```python
def save_markdown(content: str, output_path: str) -> str:
    """Save Markdown content to file with UTF-8 encoding"""

def ensure_directory(path: str) -> Path:
    """Create directory if it doesn't exist"""

def sanitize_filename(title: str) -> str:
    """Convert page title to safe filename (kebab-case)"""

def get_output_path(page_title: str, output_dir: str) -> str:
    """Generate output path from page title"""

def download_image(image_url: str, output_dir: str) -> str:
    """Download image from URL and save to output_dir/images/"""

def create_image_directory(output_path: str) -> Path:
    """Create images/ subdirectory relative to output file"""
```

**Technical Requirements:**
- UTF-8 encoding (critical for Windows compatibility)
- Handle Windows path restrictions
- Generate safe filenames from page titles (kebab-case)
- Create output directories automatically
- Handle file overwrite conflicts (warn user)
- **Image Management**:
  - Create `images/` subdirectory relative to output Markdown file
  - Download images with sanitized filenames
  - Handle image download failures gracefully
  - Validate image formats before saving
  - Generate relative paths for Markdown image references

### Configuration Management

#### Token Storage

**Primary Method: Config File**
- Location: `~/.notion-md/config.yaml`
- Format: YAML with encrypted token
- Fallback: Environment variable `NOTION_API_TOKEN`

**Security Considerations:**
- File permissions restricted to user
- Token not logged or printed
- Clear error if token missing/invalid

## Implementation Plan

### Phase 1: Research & Design (30 minutes)

**Task 1.1: Research Notion API**
- Review Notion API documentation
- Identify authentication flow
- Document block types and structure
- Understand pagination and rate limiting

**Task 1.2: Verify Development Environment**
- Confirm Python 3.13.7 available
- Verify UV package manager working
- Test basic Click CLI setup

**Deliverables:**
- Notion API integration notes
- Block type support matrix
- Development environment confirmed

### Phase 2: Core Implementation (115 minutes)

**Task 2.1: Notion API Client (30 minutes)**
- Implement `notion_client.py` module
- Add authentication handling
- Implement page and block fetching
- Add pagination support
- Error handling for API failures

**Task 2.2: Block Converter (60 minutes)**
- Implement `block_converter.py` module
- Add conversion functions for priority block types
- Handle rich text annotations
- Support nested blocks with indentation
- Implement callout → blockquote conversion
- Implement toggle → flattened text conversion
- Implement table → Markdown table conversion
- Handle internal page link placeholder conversion
- Test with sample Notion blocks

**Task 2.3: Storage Module (25 minutes)**
- Implement `storage.py` module
- Add UTF-8 file saving
- Filename sanitization (kebab-case)
- Directory creation
- Image download functionality
- Image directory management
- Relative path generation for images

**Deliverables:**
- Working API client
- Block-to-Markdown converter with special block handling
- File storage system with image download support

### Phase 3: CLI Integration (45 minutes)

**Task 3.1: CLI Framework (20 minutes)**
- Set up Click CLI structure
- Implement `configure` command
- Implement `status` command
- Add help text and error messages

**Task 3.2: Extract Command (15 minutes)**
- Implement `extract` command
- Wire together API client, converter, storage
- Add progress indicators
- Error handling and user feedback

**Task 3.3: Package Configuration (10 minutes)**
- Configure `pyproject.toml` for global install
- Set up entry points
- Add dependencies

**Deliverables:**
- Complete CLI tool
- Global installation support
- User documentation

### Phase 4: Testing & Validation (35 minutes)

**Task 4.1: Configuration Testing (5 minutes)**
- Test `configure` command
- Verify token storage
- Test `status` command

**Task 4.2: Single Page Extraction (20 minutes)**
- Extract simple page (text only)
- Extract complex page (multiple block types including callouts, tables, images)
- Verify UTF-8 encoding
- Verify image downloads working
- Test callout, toggle, and table conversions
- Test with user's actual Notion pages (Revenue Growth Machine Framework document)

**Task 4.3: Edge Case Testing (10 minutes)**
- Empty pages
- Pages with special characters in title
- Pages with unsupported block types
- Permission errors
- Network failures

**Deliverables:**
- Tested tool with user's Notion pages
- Markdown files ready for business proposal work
- Known limitations documented

### Total Timeline: ~3.5 hours

## Success Criteria

### MVP Complete When:
1. ✅ User can configure Notion API token globally
2. ✅ User can extract single Notion page to Markdown from any directory
3. ✅ Markdown output is clean and usable with Claude Code
4. ✅ UTF-8 encoding works correctly on Windows
5. ✅ All priority block types convert properly (including callouts, tables, toggles)
6. ✅ Images download locally and reference correctly in Markdown
7. ✅ Internal page links convert to placeholder text with document names
8. ✅ Tool works reliably for user's 20-25 business proposal pages

### Quality Gates:
- No crashes on valid Notion URLs
- Clear error messages for common failures
- Markdown files render correctly in VS Code
- Tool can be uninstalled cleanly for future replacement

## Risk Management

### Known Risks & Mitigations

#### Risk 1: UTF-8 Encoding Issues on Windows
- **Impact**: High (blocks usage)
- **Probability**: Medium (encountered in GitIngest agent)
- **Mitigation**: Always use `encoding='utf-8'` in file operations, test early with special characters

#### Risk 2: API Rate Limiting
- **Impact**: Medium (slows extraction)
- **Probability**: Low (single-page extraction)
- **Mitigation**: Implement exponential backoff, add progress indicators

#### Risk 3: Unsupported Block Types
- **Impact**: Medium (incomplete extraction)
- **Probability**: High (Notion has many block types)
- **Mitigation**: Log unsupported types, continue processing, document limitations

#### Risk 4: Complex Nested Structures
- **Impact**: Medium (formatting issues)
- **Probability**: Medium
- **Mitigation**: Start simple, test incrementally, focus on common cases

#### Risk 5: Image Download Failures
- **Impact**: Medium (incomplete content extraction)
- **Probability**: Medium (network issues, private images, authentication)
- **Mitigation**: Graceful error handling, log failures, continue processing, fallback to URL reference if download fails

## Future Enhancements (Post-Prototype)

### Phase 2: Enhanced CLI Tool
- Batch extraction from databases
- Automatic link following (extract referenced pages)
- Advanced block type support (databases, embedded content, column layouts, synced blocks)
- Configuration profiles for multiple workspaces
- Image optimization and compression options

### Phase 3: BMAD BMB Agent Integration
- Expert Agent wrapper using BMAD v6-alpha BMB
- Agent commands: `*extract-page`, `*configure`
- Sidecar resources: memories.md, session tracking
- IDE integration (Claude Code, Cursor)

### Phase 4: Advanced Features
- Watch mode (auto-sync Notion changes)
- Bi-directional sync (Markdown → Notion)
- Custom block type plugins
- Rich media handling
- Multi-workspace support

## Appendices

### Appendix A: Notion Block Types Reference

**Supported in MVP:**
- paragraph
- heading_1, heading_2, heading_3
- bulleted_list_item
- numbered_list_item
- quote
- callout (converted to blockquote with emoji)
- code
- divider
- image (downloaded locally)
- file
- table (converted to Markdown table format)
- toggle (flattened to text with heading)
- child_page (converted to placeholder with page name)

**Conversion Specifications:**
- **Callout**: `> 💡 **Heading** content` (blockquote format)
- **Toggle**: Flattened to heading + content
- **Table**: Markdown table with proper column alignment
- **Internal Links**: `[Page Name - see separate import]`
- **Images**: Downloaded to `./images/` with relative path references

**Deferred to Phase 2:**
- database
- embed
- video
- audio
- bookmark
- equation
- breadcrumb
- column_list
- synced_block

### Appendix B: Configuration File Format

```yaml
# ~/.notion-md/config.yaml
notion:
  api_token: "secret_xxxxxxxxxxxxxxxxxxxx"
  version: "2022-06-28"

settings:
  default_output_dir: "./notion-exports"
  filename_format: "kebab-case"
  encoding: "utf-8"
```

### Appendix C: CLI Usage Examples

```bash
# Initial setup
uv tool install .
notion-md configure --token secret_abc123xyz

# Extract to current directory (uses page title for filename)
notion-md extract https://www.notion.so/Page-Title-abc123

# Extract to specific file
notion-md extract https://www.notion.so/Page-Title-abc123 --output ~/projects/business-proposal.md

# Check configuration
notion-md status

# Uninstall when ready for v2
uv tool uninstall notion-markdown-extractor
```

### Appendix D: Error Handling Strategy

**Error Categories:**

1. **Configuration Errors**
   - Missing token → Prompt to run `configure`
   - Invalid token → Check token format, verify in Notion

2. **API Errors**
   - 401 Unauthorized → Token invalid or expired
   - 404 Not Found → Page doesn't exist or no access
   - 429 Rate Limited → Wait and retry with backoff
   - 500 Server Error → Retry with exponential backoff

3. **Conversion Errors**
   - Unsupported block type → Log warning, skip block, continue
   - Malformed block data → Log error, skip block, continue

4. **Storage Errors**
   - Permission denied → Check directory permissions
   - Disk full → Clear space or choose different output location
   - Invalid filename → Sanitize and retry

5. **Image Download Errors**
   - Network timeout → Retry with exponential backoff, fallback to URL reference
   - 403 Forbidden → Log warning, use URL reference instead of download
   - Invalid image format → Log warning, skip image
   - Download failure → Continue processing, note in output

**Error Message Format:**
```
❌ Error: [Clear description of what went wrong]
💡 Suggestion: [Actionable step to fix]
📚 Help: Run 'notion-md --help' for usage information
```

### Appendix E: Lessons from GitIngest Agent Project

**Key Learnings Applied:**

1. **UTF-8 Encoding**: Always explicit `encoding='utf-8'` on Windows
2. **Error Messages**: Clear, actionable, friendly tone
3. **Progress Indicators**: Essential for long operations
4. **Click Framework**: Proven, simple, powerful
5. **UV Package Manager**: Fast, reliable, modern
6. **Global Install**: Convenient for cross-project usage
7. **Prototype Mindset**: Ship quickly, iterate based on real usage

---

## Document Control

**Document Information:**
- **Title**: Product Requirements Document: Notion Markdown Extractor Prototype
- **Version**: 1.2
- **Status**: ✅ Complete (MVP Implemented)
- **Created**: 2025-10-06
- **Last Modified**: 2026-01-05
- **Author**: Claude Code (with Drew A.)
- **Project**: notion-markdown-extractor
- **File Location**: `plan/prd-notion-md-extractor-prototype-2025-10-06.md`

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-06 | Claude Code | Initial PRD based on draft project plan and user discussion |
| 1.1 | 2025-10-06 | Claude Code | Updated based on sample Notion page analysis: Added image download requirement (FR5), updated block type support (tables, callouts, toggles), added conversion specifications, updated timeline to 3.5 hours, added image handling technical details |
| 1.2 | 2026-01-05 | Claude Code | MVP complete: Added ✅ status markers to all FRs, documented implemented-beyond-scope features (synced blocks, auto-directory, rate limiting), updated document status to Complete |

**Approval:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Product Owner | Drew A. | Pending | |
| Technical Lead | Claude Code | 2025-10-06 | ✓ |

**Related Documents:**
- Original draft plan: `user-context/notion-md-cli-project-plan-2025-10-06.md`
- Workspace guidelines: `../../CLAUDE.md`
- README: `README.md`

**Distribution:**
- Drew A. (Product Owner)
- Claude Code implementation sessions
- Future BMAD BMB agent development

**Document Classification:** Internal - Project Planning

**Keywords:** notion, markdown, extraction, cli, prototype, prd, python, api-integration