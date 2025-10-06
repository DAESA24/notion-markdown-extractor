# BMAD v6-alpha CIS Module - Minimal Installation Guide

## Quick Answer: What You Need

To use the **Creative Intelligence System (CIS)** module from BMAD v6-alpha, you need:

### Minimum Requirements:

1. **BMAD Core** (`src/core/`) - Contains the brainstorming workflow
2. **CIS Module** (`src/modules/cis/`) - Contains CIS-specific workflows and agents
3. **Module Installer** - To compile and deploy to your project

**Important**: The **brainstorming workflow is actually in BMAD Core**, not CIS! CIS just references and extends it with specialized agents.

## What is CIS?

The Creative Intelligence System provides **AI-powered creative facilitation** through 5 specialized domains:

### 5 Core Workflows:
1. **Brainstorming** - 36 creative techniques (in BMAD Core, shared with CIS)
2. **Design Thinking** - 5-phase human-centered design
3. **Problem Solving** - Root cause analysis
4. **Innovation Strategy** - Business model disruption
5. **Storytelling** - 25 narrative frameworks

### 5 Specialized Agents:
1. **Carson** - Elite Brainstorming Specialist (energetic facilitator)
2. **Maya** - Design Thinking Maestro (jazz-like improviser)
3. **Dr. Quinn** - Master Problem Solver (detective-scientist)
4. **Victor** - Disruptive Innovation Oracle (bold strategist)
5. **Sophia** - Master Storyteller (whimsical narrator)

## Key Insight: Brainstorming is Core, Not CIS

```
src/
├── core/
│   └── workflows/
│       └── brainstorming/          ← The 36-technique workflow
│           ├── workflow.yaml
│           ├── instructions.md
│           ├── template.md
│           └── brain-methods.csv   ← Database of techniques
├── modules/
    └── cis/
        ├── agents/                  ← Carson, Maya, etc.
        ├── workflows/               ← Other 4 workflows
        └── _module-installer/
```

**Why this matters**: You can use the brainstorming workflow **without CIS** if you only install BMAD Core!

## Installation Options

### Option 1: Full v6-alpha Installation (Unstable)

**What you get**: Complete BMAD v6 system with CIS module

**Process**:
```bash
git clone https://github.com/bmad-code-org/BMAD-METHOD.git
cd BMAD-METHOD
git checkout v6-alpha
npm install
npm run installer
# Select: Install CIS module
```

**Pros**:
- Complete system
- All 5 CIS workflows
- All 5 CIS agents

**Cons**:
- v6-alpha is unstable (daily changes)
- Complex setup
- Requires full BMAD infrastructure
- Breaking changes likely

### Option 2: Manual Cherry-Pick (Recommended for Your Use Case)

**What you get**: Just the workflows/agents you need

**Process**:
1. Clone v6-alpha repo
2. Copy specific workflow folders to your project
3. Create simple wrapper to invoke them
4. Skip full BMAD installation

**Files to Copy for Brainstorming**:
```
Your Project/
└── bmad-workflows/
    └── brainstorming/
        ├── workflow.yaml
        ├── instructions.md
        ├── template.md
        └── brain-methods.csv
```

**Pros**:
- Minimal dependencies
- No full BMAD installation needed
- Stable (copied files won't change)
- Use today

**Cons**:
- Missing agent personas (Carson, etc.)
- Manual updates if v6 changes
- No automatic compilation

### Option 3: Wait for Stable v6 Release

**Timeline**: Mid-October 2025 (per v6-alpha README)

**What you get**: Official stable release with proper installer

**Pros**:
- Stable, tested system
- Proper npm package
- Official support

**Cons**:
- Have to wait ~1 week
- Can't use now for business proposal

## Minimal Dependencies Breakdown

### To Use Brainstorming Workflow Only:

**Required Files**:
- `src/core/workflows/brainstorming/*` (4 files)
- Optional: `/bmad/cis/config.yaml` for configuration

**Required Configuration**:
```yaml
# /bmad/cis/config.yaml
output_folder: "./brainstorming-sessions"
user_name: "Drew"
communication_language: "English"
```

**No Need For**:
- Full BMAD Core agents
- CIS module agents (unless you want Carson's personality)
- Module installer (if manually copying)
- Other workflows (design thinking, problem solving, etc.)

### To Use Full CIS Module:

**Required Files**:
- Everything in `src/core/` (BMAD Core)
- Everything in `src/modules/cis/` (CIS Module)
- Node.js build system for compilation
- BMAD installer infrastructure

**Configuration**:
- `/bmad/core/config.yaml` (core configuration)
- `/bmad/cis/config.yaml` (CIS configuration)

## Practical Recommendation for Your Needs

Based on your immediate need for **business proposal work** and interest in **creative brainstorming**:

### Best Approach: Hybrid Strategy

1. **Today**: Use ChatGPT/Claude with brainstorming prompt
   - Copy the 36 techniques from `brain-methods.csv`
   - Create a simple prompt template
   - No installation needed
   - Use immediately

2. **This Week**: Build Notion extraction tool (your priority)
   - Focus on business proposal extraction
   - Get working tool quickly

3. **Mid-October**: Install stable BMAD v6 with CIS
   - Wait for official beta release
   - Proper installation via npm
   - All 5 workflows + 5 agents
   - Integrate with your workflow

### Interim Solution: DIY Brainstorming Prompt

You can **replicate CIS brainstorming today** without any installation:

**Simple Prompt Template**:
```
You are Carson, an elite brainstorming facilitator with infectious energy
and a master of 36 creative techniques.

Techniques available:
[List from brain-methods.csv]

Guide me through a brainstorming session on: [TOPIC]

Use "Yes, and..." methodology. Ask questions to draw out my ideas.
Generate 100 ideas in 60 minutes. Check my energy every 15 minutes.

Start by asking what specific brainstorming technique I want to use,
or recommend one based on my topic.
```

## The 36 Brainstorming Techniques (Quick Reference)

From BMAD Core's `brain-methods.csv`:

### Collaborative (4)
- Yes And Building, Brain Writing Round Robin, Random Stimulation, Role Playing

### Structured (4)
- SCAMPER Method, Six Thinking Hats, Mind Mapping, Resource Constraints

### Creative (7)
- What If Scenarios, Analogical Thinking, Reversal Inversion, First Principles,
  Forced Relationships, Time Shifting, Metaphor Mapping

### Deep Analysis (5)
- Five Whys, Morphological Analysis, Provocation Technique,
  Assumption Reversal, Question Storming

### Theatrical (5)
- Time Travel Talk Show, Alien Anthropologist, Dream Fusion Lab,
  Emotion Orchestra, Parallel Universe Cafe

### Wild Methods (5)
- Chaos Engineering, Guerrilla Gardening Ideas, Pirate Code Brainstorm,
  Zombie Apocalypse Planning, Drunk History Retelling

### Introspective (6)
- Inner Child Conference, Shadow Work Mining, Values Archaeology,
  Future Self Interview, Body Wisdom Dialogue

## How CIS Workflows Actually Work

### Workflow Invocation Pattern:

```bash
# If you had full v6-alpha installed:
workflow brainstorming
workflow brainstorming --data /path/to/context.md

# Or via agent:
agent cis/brainstorming-coach
> *brainstorm
```

### What Happens Behind the Scenes:

1. **Reads config** from `/bmad/cis/config.yaml`
2. **Loads instructions** from `workflow.yaml` and `instructions.md`
3. **References techniques** from `brain-methods.csv`
4. **Follows 8-phase process**:
   - Setup (context gathering)
   - Approach selection (technique choice)
   - Interactive facilitation (idea generation)
   - Convergent organization (categorization)
   - Insight extraction (pattern identification)
   - Action planning (prioritization)
   - Session reflection (analysis)
   - Report generation (structured output)
5. **Saves report** to configured output folder

### Key Differentiators from Regular Prompting:

- **Structured phases** ensure complete exploration
- **Energy monitoring** adapts to user engagement
- **36 proven techniques** provide systematic creativity
- **Context integration** for domain-specific guidance
- **Action planning** converts ideas to next steps
- **Session documentation** creates shareable reports

## Configuration Files Explained

### `/bmad/cis/config.yaml`
```yaml
output_folder: "./creative-sessions"  # Where results save
user_name: "Drew"                     # Who's brainstorming
communication_language: "English"     # Facilitation language
```

### Why Configuration Matters:
- **output_folder**: Organizes all brainstorming sessions
- **user_name**: Personalizes facilitation ("Great thinking, Drew!")
- **communication_language**: Enables multilingual support

## Summary: What You Should Do

### For Immediate Creative Brainstorming:
**Option**: Use ChatGPT/Claude with the 36 techniques list
**Time**: 5 minutes to set up
**Benefit**: Works today, no installation

### For Business Proposal (Your Priority):
**Option**: Build Notion extraction tool (per your project plan)
**Time**: ~3.5 hours
**Benefit**: Extract Notion pages → Markdown for Claude Code work

### For Long-term CIS Integration:
**Option**: Wait for stable BMAD v6 release (mid-October)
**Time**: 1 week wait
**Benefit**: Official, stable, supported installation

## Files You'd Need to Copy (If Cherry-Picking)

### Core Brainstorming Only:
```
src/core/workflows/brainstorming/
├── workflow.yaml           (workflow configuration)
├── instructions.md         (8-phase execution guide)
├── template.md            (session report structure)
└── brain-methods.csv      (36 techniques database)
```

**Total**: 4 files, ~500 lines total

### Full CIS Module:
```
src/core/                   (entire core system)
src/modules/cis/           (entire CIS module)
```

**Total**: ~50+ files, thousands of lines

## Questions Answered

**Q: Can I use CIS without full BMAD v6?**
A: The brainstorming workflow can work standalone, but other workflows need BMAD infrastructure.

**Q: What's the absolute minimum to get brainstorming working?**
A: Copy 4 files from `src/core/workflows/brainstorming/` + create simple config.

**Q: Do I need the CIS agents (Carson, Maya, etc.)?**
A: No - they're optional persona wrappers. Workflows work without them.

**Q: Is v6-alpha stable enough to use?**
A: No - it's alpha with daily changes. Use for experimentation only.

**Q: Should I wait for stable v6?**
A: Yes, if you can wait ~1 week. Mid-October 2025 is target release.

**Q: Can I use this for my business proposal work now?**
A: Better to use ChatGPT/Claude with technique list today. Install v6 properly later.

## Next Steps

1. ✅ **Understand what CIS offers** (you've done this)
2. ⏭️ **Build Notion extraction tool** (your immediate priority)
3. ⏭️ **Experiment with brainstorming techniques** (use ChatGPT/Claude with list)
4. ⏭️ **Monitor v6 release** (mid-October for stable version)
5. ⏭️ **Install v6 properly** when stable (full CIS benefits)

---

*Created 2025-10-06 based on BMAD v6-alpha source code analysis and user's business proposal needs.*
