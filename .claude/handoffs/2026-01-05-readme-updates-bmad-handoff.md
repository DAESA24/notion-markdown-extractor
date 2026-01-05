---
handoff_id: 2026-01-05-readme-updates-bmad-handoff
type: bmad
created: 2026-01-05 17:30
status: pickup_completed
workspace: c:\Users\drewa\work\dev\notion-markdown-extractor
pickup_history:
  - date: 2026-01-05 18:00
    notes: "Completed all 7 README updates"
bmad_workflow:
  state: between_workflows
  completed_workflow: null
  next_workflow: null
  next_agent: null
  workflow_outputs:
    - path: "docs/project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md"
      description: "PRD updated to v1.2 with MVP completion status"
    - path: "execute/src/notion_markdown_extractor/project_detector.py"
      description: "Simplified - removed dead code"
    - path: "README.md"
      description: "Partially updated - legacy terminology removed"
    - path: "docs/user-docs/usage.md"
      description: "Updated - legacy terminology removed"
    - path: "docs/user-docs/notion-setup.md"
      description: "Updated - legacy terminology removed"
---

# BMAD Workflow Handoff: README Updates

- **Created:** 2026-01-05 17:30
- **Purpose:** Complete README.md cleanup and improvements
- **Status:** Handoff - Ready for pickup

## Resume Instructions

**This is a documentation task, not a formal BMAD workflow.**

### To Resume

1. Open this project in Claude Code
2. Read this handoff document
3. Execute the README updates listed below

## Workflow State

| Field | Value |
|-------|-------|
| **State** | Between Workflows |
| **Context** | PRD review and doc cleanup session |
| **Recommended Next** | Direct README updates (not a formal workflow) |

## Session Accomplishments

This session completed:

1. **PRD Review** - Verified all functional requirements (FR1-FR5) are implemented
2. **PRD Update** - Marked as v1.2 with ✅ completion status, documented beyond-MVP features
3. **Code Cleanup** - Simplified `project_detector.py`, removed dead "Software Projects"/"Thought Projects" detection
4. **Doc Updates** - Removed legacy terminology from README.md, usage.md, notion-setup.md
5. **Commits** - 3 commits pushed to main

## Next Actions: README.md Updates

The following 7 updates were approved but not yet implemented:

### 1. Fix Documentation Links

Current (broken):
```markdown
- **[Usage Guide](docs/usage.md)**
- **[Notion Setup Guide](docs/notion-setup.md)**
```

Should be:
```markdown
- **[Usage Guide](docs/user-docs/usage.md)**
- **[Notion Setup Guide](docs/user-docs/notion-setup.md)**
```

### 2. Fix Project Doc Links

Current (broken):
```markdown
- **[PRD](plan/prd-notion-md-extractor-prototype-2025-10-06.md)**
- **[Project Checkpoints](project-checkpoints/)**
- **[Workspace Guidelines](../../CLAUDE.md)**
```

Should be:
```markdown
- **[PRD](docs/project-planning-artifacts/prd-notion-md-extractor-prototype-2025-10-06.md)**
```
(Remove project-checkpoints and CLAUDE.md references - broken/irrelevant)

### 3. Status Consistency

- Remove all "prototype" mentions
- Use "MVP Complete" consistently
- Update footer line from "Prototype - Fast extraction..." to "MVP Complete"

### 4. Consolidate "How Auto-Directory Works" Section

Either cut entirely or consolidate into Quick Start section. The content is redundant with Overview and Features.

### 5. Update Roadmap Section

Current:
```markdown
### Current: Prototype (v0.1)
...
### Future: Enhanced Version (v2.0)
```

Should be:
```markdown
### MVP
...
### Future: Enhanced Version
```
(Remove version numbers)

### 6. Add Table of Contents

Add at top of README with internal anchor links to major sections.

### 7. Add BMAD Credit

Add a section crediting the BMAD framework:
- Description: "AI-driven agile development framework"
- Repo URL: https://github.com/bmad-code-org/BMAD-METHOD

## Key Decisions Made

- Removed "Software Projects" / "Thought Projects" terminology entirely - tool works from any directory
- PRD marked as complete (v1.2) - MVP is done
- Simplified project_detector.py - detection logic was dead code

## Session Notes

- Drew prefers direct, specific feedback
- All changes should use conventional commits
- The BMAD PM agent was invoked but work was done outside formal workflows
