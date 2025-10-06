# Documentation TODO

Tracking remaining documentation to be created for the Notion Markdown Extractor project.

## Phase 1: Essential User Docs ✅ COMPLETE

- [x] **README.md** - Project overview and quick start
- [x] **docs/usage.md** - Complete CLI reference
- [x] **docs/notion-setup.md** - Integration setup and permissions guide

---

## Phase 2: Extended User Documentation

### Priority: High
- [ ] **docs/troubleshooting.md** - Common issues and solutions
  - API permission errors
  - Encoding issues
  - Missing content scenarios
  - How to report bugs
  - FAQ section

- [ ] **docs/features.md** - Detailed feature reference
  - Supported block types with examples
  - Unsupported block types and workarounds
  - Image handling details
  - Rich text formatting capabilities
  - Synced blocks explanation
  - Limitations and known issues

### Priority: Medium
- [ ] **docs/examples.md** - Real-world usage examples
  - Thought Project workflows
  - Software Project workflows
  - Batch extraction scripts
  - Integration with other tools
  - Advanced use cases

---

## Phase 3: Developer Documentation

### Priority: High
- [ ] **docs/architecture.md** - System design overview
  - Module structure and responsibilities
  - Data flow (Notion API → Blocks → Markdown → File)
  - Key components:
    - NotionClient
    - BlockConverter
    - Storage
    - ProjectDetector
    - Config
  - Design decisions and rationale

- [ ] **docs/development.md** - Developer setup guide
  - Local development environment setup
  - Running without installation
  - Development workflow
  - Testing locally
  - Debugging tips
  - Using `uv tool install . --force --reinstall`

### Priority: Medium
- [ ] **CONTRIBUTING.md** - Contribution guidelines
  - How to fork and clone
  - Feature branch workflow
  - Code style guidelines
  - Commit message format
  - Pull request requirements
  - Review process

- [ ] **docs/api-reference.md** - Code API documentation
  - Module documentation
  - Class definitions and methods
  - Parameters and return types
  - Usage examples for each class
  - Extension points

### Priority: Low
- [ ] **docs/block-converters.md** - Adding new block types
  - Step-by-step tutorial
  - Example: Adding a converter
  - Testing your converter
  - Markdown conversion rules
  - Handling nested blocks

- [ ] **docs/testing.md** - Testing guide
  - Running tests
  - Writing new tests
  - Test coverage requirements
  - Mocking Notion API responses

---

## Phase 4: Advanced Documentation

### Priority: Low
- [ ] **docs/integration.md** - Integration with other tools
  - CI/CD pipelines
  - Git hooks
  - BMAD workflow integration
  - MCP server considerations

- [ ] **docs/changelog.md** - Version history
  - Release notes format
  - Breaking changes tracking
  - Migration guides

- [ ] **docs/security.md** - Security best practices
  - Token management
  - Access control
  - Audit logging
  - Data privacy considerations

---

## Documentation Infrastructure

### Tools & Automation
- [ ] Setup documentation linting
- [ ] Add link checking
- [ ] Generate API docs from docstrings
- [ ] Setup documentation site (MkDocs/Sphinx)
- [ ] Add search functionality

### Quality
- [ ] Review all docs for consistency
- [ ] Add screenshots/diagrams where helpful
- [ ] Ensure all code examples are tested
- [ ] Cross-reference between docs
- [ ] Add table of contents to longer docs

---

## Notes

### Style Guidelines
- Use clear, concise language
- Include practical examples
- Provide troubleshooting steps
- Link between related docs
- Keep navigation easy

### Priority Definitions
- **High**: Blocks user adoption or contribution
- **Medium**: Improves user/developer experience
- **Low**: Nice-to-have enhancements

### Review Cadence
- Phase 1: Complete ✅
- Phase 2: Target after user feedback on MVP
- Phase 3: Target when seeking contributors
- Phase 4: Target for v2.0 release

---

**Last Updated**: 2025-10-06
**Status**: Phase 1 Complete, Phases 2-4 Pending
