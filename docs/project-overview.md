# Project Overview

- **Project:** notion-markdown-extractor
- **Version:** 0.1.0 (Prototype)
- **Status:** MVP Complete
- **Generated:** 2026-01-04

## Purpose

A Python CLI tool that extracts Notion pages and converts them to Markdown files with automatic project organization. Built for seamless integration with Claude Code workflows.

## Quick Reference

| Property | Value |
|----------|-------|
| **Type** | CLI Tool (Monolith) |
| **Language** | Python 3.12+ |
| **Framework** | Click CLI |
| **Package Manager** | UV |
| **Entry Point** | `notion-md` |
| **Config Location** | `~/.notion-md/config.yaml` |

## Key Features

- **Auto-directory creation** - Saves to `user-context/notion-pages/`
- **Local image downloads** - Images downloaded with relative paths
- **Rich block support** - Callouts, tables, toggles, synced blocks
- **Project-aware** - Detects Software/Thought projects
- **Global CLI** - Works from any directory

## Commands

| Command | Description |
|---------|-------------|
| `notion-md extract <url>` | Extract page to Markdown |
| `notion-md configure --token <token>` | Save API token |
| `notion-md status` | Show configuration status |

## Module Summary

| Module | Purpose |
|--------|---------|
| `cli.py` | CLI commands |
| `config.py` | Token management |
| `notion_client.py` | Notion API wrapper |
| `block_converter.py` | Block → Markdown conversion |
| `storage.py` | File I/O, image downloads |
| `project_detector.py` | Project type detection |

## Documentation Links

### Generated Documentation
- [Architecture](./architecture.md) - System design and patterns
- [Source Tree Analysis](./source-tree-analysis.md) - Project structure
- [Development Guide](./development-guide.md) - Setup and development

### User Documentation
- [Usage Guide](./user-docs/usage.md) - CLI reference
- [Notion Setup](./user-docs/notion-setup.md) - Integration setup
- [TODO / Roadmap](./user-docs/TODO.md) - Future features

### Planning Artifacts
- [PRD](./project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md) - Product requirements

### Reference
- [Notion API Docs](./notion-api-docs/) - 32 crawled API reference files

## Roadmap

### Current: v0.1.0 (Prototype)
- Single-page extraction
- Local image downloads
- Core block types
- Global CLI installation

### Future: v2.0 (Enhanced)
- Batch extraction from databases
- Automatic link following
- Advanced block types
- Multi-workspace support
