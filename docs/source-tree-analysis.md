# Source Tree Analysis

- **Project:** notion-markdown-extractor
- **Type:** CLI Tool (Monolith)
- **Generated:** 2026-01-04

## Project Structure

```
notion-markdown-extractor/
├── execute/                          # Implementation directory
│   ├── src/
│   │   └── notion_markdown_extractor/  # Main package
│   │       ├── __init__.py           # Package init, exports main()
│   │       ├── cli.py                # [ENTRY] Click CLI commands
│   │       ├── config.py             # Configuration management
│   │       ├── notion_client.py      # Notion API wrapper
│   │       ├── block_converter.py    # Block → Markdown conversion
│   │       ├── storage.py            # File I/O operations
│   │       └── project_detector.py   # Project type detection
│   ├── tests/                        # Test suites (to be added)
│   ├── pyproject.toml                # UV project config
│   ├── uv.lock                       # Dependency lock file
│   ├── .python-version               # Python version (3.12+)
│   └── README.md                     # Execute-specific readme
│
├── docs/                             # Documentation
│   ├── project-planning-artifacts/   # PRD and planning docs
│   │   └── prd-notion-md-extractor-prototype-2025-10-06.md
│   ├── user-docs/                    # End-user documentation
│   │   ├── usage.md                  # CLI usage guide
│   │   ├── notion-setup.md           # Notion integration setup
│   │   └── TODO.md                   # Feature roadmap
│   └── notion-api-docs/              # Notion API reference (32 files)
│       ├── block.md, page.md, database.md, ...
│       └── (crawled from developers.notion.com)
│
├── project-checkpoints/              # Development session notes
│   ├── post-synced-block-fix-checkpoint-2025-10-06.md
│   └── synced-block-debugging-checkpoint-2025-10-06.md
│
├── user-context/                     # Context files for AI
│   └── notion-md-cli-project-plan-2025-10-06.md
│
├── _bmad/                            # BMad Method framework
│   └── bmm/                          # BMM module installation
│       ├── agents/                   # BMAD agent definitions
│       ├── workflows/                # BMAD workflow definitions
│       └── config.yaml               # BMM configuration
│
├── .claude/                          # Claude Code configuration
│   ├── settings.local.json           # Local settings
│   └── handoffs/                     # Session handoff files
│
├── README.md                         # Project README
├── .gitignore                        # Git ignore rules
└── .mcp.json                         # MCP server configuration
```

## Critical Directories

| Directory | Purpose | Key Files |
|-----------|---------|-----------|
| `execute/src/notion_markdown_extractor/` | **Core source code** | All Python modules |
| `docs/user-docs/` | End-user documentation | usage.md, notion-setup.md |
| `docs/project-planning-artifacts/` | Planning documents | PRD |
| `project-checkpoints/` | Dev session notes | Debugging logs |

## Module Responsibilities

### Core Modules (`execute/src/notion_markdown_extractor/`)

| Module | Responsibility | Dependencies |
|--------|----------------|--------------|
| `cli.py` | CLI commands (extract, configure, status) | click, config, notion_client, storage |
| `config.py` | Token storage in `~/.notion-md/` | yaml, pathlib |
| `notion_client.py` | Notion API wrapper | notion-client SDK |
| `block_converter.py` | Block → Markdown conversion | None (pure logic) |
| `storage.py` | File writes, image downloads | requests, pathlib |
| `project_detector.py` | Detect Software/Thought projects | pathlib |

## Entry Point

```
notion-md → notion_markdown_extractor:main (cli.py)
         ↓
    Click Group
         ├── extract   # Main extraction command
         ├── configure # Token configuration
         └── status    # Show config status
```

## Data Flow

```
User runs: notion-md extract <url>
         ↓
    cli.py parses URL, loads config
         ↓
    notion_client.py fetches page + blocks
         ↓
    block_converter.py converts blocks → markdown
         ↓
    storage.py writes .md file + downloads images
         ↓
    Output: user-context/notion-pages/<page>.md
```

## File Counts

| Category | Count |
|----------|-------|
| Source modules | 7 |
| Documentation files | 41 (9 project + 32 API ref) |
| Dev checkpoints | 2 |
| Total tracked files | ~50 |
