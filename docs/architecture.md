# Architecture Documentation

- **Project:** notion-markdown-extractor
- **Type:** CLI Tool
- **Version:** 0.1.0 (Prototype)
- **Generated:** 2026-01-04

## Executive Summary

A Python CLI tool that extracts Notion pages to Markdown format with local image downloads. Built for integration with Claude Code workflows, featuring auto-directory organization and project-aware file placement.

## Technology Stack

| Category | Technology | Version |
|----------|------------|---------|
| Language | Python | 3.12+ |
| CLI Framework | Click | 8.3.0+ |
| Notion SDK | notion-client | 2.5.0+ |
| Package Manager | UV | Latest |
| Build System | uv_build | 0.8.22+ |

## Architecture Pattern

**Pattern:** Command-Line Interface with Pipeline Architecture

The tool follows a simple pipeline pattern:
1. **Input** → Parse URL/command args
2. **Fetch** → Retrieve page and blocks from Notion API
3. **Transform** → Convert blocks to Markdown
4. **Output** → Write files to disk

## Module Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLI Layer                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                     cli.py                               ││
│  │  • extract command   • configure command   • status cmd  ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  config.py    │    │notion_client.py│   │project_detector│
│               │    │               │    │     .py       │
│ Token storage │    │ API wrapper   │    │ Directory     │
│ ~/.notion-md/ │    │ Page/block    │    │ detection     │
│               │    │ fetching      │    │               │
└───────────────┘    └───────┬───────┘    └───────────────┘
                              │
                              ▼
                    ┌───────────────┐
                    │block_converter│
                    │     .py       │
                    │               │
                    │ Block→Markdown│
                    │ conversion    │
                    └───────┬───────┘
                              │
                              ▼
                    ┌───────────────┐
                    │  storage.py   │
                    │               │
                    │ File writes   │
                    │ Image download│
                    └───────────────┘
```

## Data Flow

### Extract Command Flow

```
notion-md extract <url>
         │
         ▼
    ┌─────────────┐
    │ cli.py      │ Parse URL, validate, load config
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │ config.py   │ Load token from ~/.notion-md/ or $NOTION_API_TOKEN
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │ project_    │ Detect if in Software/Thought project
    │ detector.py │ Determine output path
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │ notion_     │ Fetch page metadata
    │ client.py   │ Fetch all blocks (recursive)
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │ block_      │ Convert each block to Markdown
    │ converter.py│ Handle nesting, formatting
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │ storage.py  │ Write .md file
    └──────┬──────┘ Download images locally
           │
           ▼
    Output: user-context/notion-pages/<title>.md
            user-context/notion-pages/images/<image>.png
```

## Key Design Decisions

### 1. User Home Configuration
- Token stored in `~/.notion-md/config.yaml`
- Not in project repo (security)
- Environment variable fallback supported

### 2. Auto-Directory Organization
- Detects "Software Projects" or "Thought Projects"
- Creates `user-context/notion-pages/` structure
- Consistent across all projects

### 3. Local Image Downloads
- Images downloaded to `images/` subfolder
- Markdown references use relative paths
- Works offline after extraction

### 4. Click Framework
- Declarative command definition
- Built-in help generation
- Easy to extend with new commands

## Block Type Support

### Fully Supported
- Paragraphs, Headings (1-3), Quotes
- Bulleted/Numbered lists (with nesting)
- Code blocks (with syntax highlighting)
- Images (downloaded locally)
- Tables, Callouts, Toggle blocks
- Dividers, Links

### Partially Supported
- Synced blocks (content extracted)
- Internal links (placeholder text)

### Not Yet Supported
- Databases (inline and full-page)
- Embedded content, Video/Audio
- Column layouts (flattened)

## Error Handling

| Scenario | Handling |
|----------|----------|
| Invalid token | Clear error message, exit |
| Page not found | Error with sharing instructions |
| Image download fails | Log warning, continue |
| Network error | Retry logic in notion-client SDK |

## Security Considerations

- Token never stored in repo
- Config file permissions: 600 (Unix)
- No sensitive data in output files

## Future Architecture (v2.0)

Planned enhancements:
- Batch extraction from databases
- Link following (recursive page extraction)
- Multi-workspace support
- Plugin architecture for custom block types
