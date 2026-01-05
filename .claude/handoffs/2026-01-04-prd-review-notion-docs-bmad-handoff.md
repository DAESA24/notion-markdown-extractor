---
handoff_id: 2026-01-04-prd-review-notion-docs-bmad-handoff
type: bmad
created: 2026-01-04 18:45
status: pickup_completed
workspace: c:\Users\drewa\work\dev\notion-markdown-extractor
pickup_history: []
bmad_workflow:
  state: between_workflows
  completed_workflow: null
  next_workflow: create-prd
  next_agent: pm
  next_workflow_path: "_bmad/bmm/workflows/create-prd.md"
  workflow_outputs:
    - path: "docs/project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md"
      description: "Existing PRD for Notion Markdown Extractor v2.0"
    - path: "docs/notion-api-docs/"
      description: "32 crawled Notion API documentation files (5 have incomplete content)"
---

# BMAD Workflow Handoff: PRD Review for Notion API Documentation Needs

- **Created:** 2026-01-04 18:45
- **Purpose:** Review PRD v2.0 requirements to determine if 5 problematic Notion API docs are needed
- **Status:** Handoff - Ready for pickup

## Resume Instructions

**CRITICAL: Resume via BMAD workflow, not by working in this document.**

### To Resume

1. Invoke PM agent: `/bmad:bmm:agents:pm`
2. Say: "Review the existing PRD at `docs/project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md` to determine if any v2.0 requirements depend on these 5 Notion API documentation pages that have incomplete content"
3. Provide the list of problematic pages (see below)

## Workflow State

| Field | Value |
|-------|-------|
| **State** | Between Workflows |
| **Recommended Next** | PRD review with PM agent |
| **PRD Location** | `docs/project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md` |

### Context for Next Workflow

**Background:** Crawled 32 Notion API documentation pages for reference when building v2.0. Five pages have SPA routing issues that cause incomplete content capture:

| Page | URL | Issue |
|------|-----|-------|
| post-database-query.md | `/reference/post-database-query` | Content degrades toward bottom |
| query-a-data-source.md | `/reference/query-a-data-source` | Content degrades toward bottom |
| retrieve-a-data-source.md | `/reference/retrieve-a-data-source` | Content degrades toward bottom |
| retrieve-a-database.md | `/reference/retrieve-a-database` | Content degrades toward bottom |
| create-a-data-source.md | `/reference/create-a-data-source` | Content degrades toward bottom |

**Question for PM:** Do any v2.0 requirements in the PRD depend on these 5 database/data_source API endpoints? If not, we can deprioritize fixing the crawl issues.

**Note:** These pages relate to Notion's 2025-09-03 API version that introduced `data_source_id` (replacing `database_id`). If v2.0 doesn't require this migration, these docs may not be needed.

### Available Documentation (27 pages with complete content)

The following Notion API docs were successfully crawled and are available in `docs/notion-api-docs/`:
- block.md, page.md, database.md, data-source.md
- property-object.md, property-item-object.md, page-property-values.md
- rich-text.md, parent-object.md, file-object.md
- post-database-query-filter.md, post-database-query-sort.md
- filter-data-source-entries.md, sort-data-source-entries.md
- working-with-databases.md, working-with-page-content.md, working-with-files-and-media.md
- upgrade-guide-2025-09-03.md, intro.md, getting-started.md
- retrieve-a-block.md, get-block-children.md, retrieve-a-page.md
- status-codes.md, request-limits.md, retrieving-files.md, importing-external-files.md

## Key Decisions Made

- Created `batch_spa_to_markdown.py` script in PBC for SPA crawling with session-based navigation
- Session-based navigation (js_only mode) improves SPA crawling but doesn't fully solve content degradation
- Decided to verify documentation needs against PRD before investing more time in crawl fixes

## Session Notes

**Technical work completed:**
- Created new Crawl4AI script: `c:\Users\drewa\pbcs\pbc-web-crawling\tool-crawl4ai\scripts\batch_spa_to_markdown.py`
- Uses session-based navigation with `js_only=True` to handle React SPA routing issues
- Auto-derives init URL or accepts `--init-url` parameter
- Includes content validation against URL patterns

**Root cause of SPA issues:** Notion's React documentation site has client-side routing bugs where direct URL access renders incorrect content. Session-based navigation (initializing router first, then navigating via JS) partially solves this but content still degrades toward page bottom.