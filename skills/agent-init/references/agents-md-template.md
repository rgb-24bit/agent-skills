# AGENTS.md Template

## Standard Structure

Use this template to generate AGENTS.md files. Adjust sections based on project needs while maintaining the core structure.

---

```markdown
# AGENTS.md

## Project Purpose

[2-3 sentences capturing:]
- Core business/technical goals
- Primary users/consumers
- Key constraints (business, technical, regulatory)

## Tech Stack and Architecture

**Languages & Frameworks:**
- [Language] [version]
- [Framework] [version]
- [Runtime requirements]

**Directory Structure:**
- `dir1/` - [One sentence describing responsibility and typical usage]
- `dir2/` - [One sentence describing responsibility and typical usage]
- `dir3/` - [One sentence describing responsibility and typical usage]

## How to Work on This Project

### Development & Run
- Working directory: [directory]
- Start dev: `[command]`
- [Additional critical command if needed]

### Testing & Quality
- Run tests: `[command]`
- Type check: `[command]` (if applicable)
- Build check: `[command]`
- For detailed test strategy, see [doc path or file:line]

### Change Validation
Before committing/raising MR:
1. [Validation step 1]
2. [Validation step 2]
3. [CI checks that must pass]

## Task-Specific Documentation

Before implementing changes, read relevant docs:
- `path/to/doc1.md` - [Purpose and when to read]
- `path/to/doc2.md` - [Purpose and when to read]
- `path/to/doc3.md` - [Purpose and when to read]

## Working Guidelines for the Agent

1. [High-leverage guideline 1]
2. [High-leverage guideline 2]
3. [High-leverage guideline 3]
4. [High-leverage guideline 4]
5. [High-leverage guideline 5] (if needed)
6. [High-leverage guideline 6] (if needed)
7. [High-leverage guideline 7] (if needed)
```

---

## Section Guidelines

### Project Purpose
- Focus on WHY the project exists
- Avoid generic descriptions
- Be specific about users and constraints
- Keep to 2-3 sentences

**Good Example:**
> This is a real-time collaboration platform for distributed teams, solving the problem of synchronous document editing across time zones. Primary users are product teams at remote-first companies. Core constraint: must handle 10k+ concurrent users with <100ms latency.

**Bad Example:**
> This is a web application for collaboration. It uses modern technologies and follows best practices.

### Tech Stack and Architecture
- List main technologies with versions
- Directory descriptions should be one sentence
- Focus on WHAT, not HOW
- Highlight shared libraries and key modules

### How to Work
- Only include 1-3 most important commands per section
- Use pointers for detailed information
- Mention linter/formatter config locations
- Specify validation requirements clearly

### Task-Specific Documentation
- List docs agent will need frequently
- One line per doc: purpose + when to read
- Prefer existing documentation over creating new
- Use relative paths from project root

### Working Guidelines
- 3-7 high-leverage rules
- Focus on behavior, not style
- Make rules actionable and specific
- Avoid obvious or low-impact rules

**High-Impact Guidelines:**
- "Before modifying shared modules, read the architecture doc at `docs/architecture.md`"
- "For changes affecting >3 files, first propose a plan listing files and rationale"
- "Run `npm run typecheck` after any TypeScript changes"

**Low-Impact Guidelines:**
- "Write clean code" (too vague)
- "Always add comments" (not universally applicable)
- "Use descriptive variable names" (obvious)

## Optional Patterns

### Per-Directory AGENTS.md
For large projects with distinct subsystems:
- Place AGENTS.md in critical subdirectories
- Keep root AGENTS.md minimal
- Example: `src/persistence/AGENTS.md` for database module

### Minimal Root Fallback
For projects with centralized documentation:
- Root AGENTS.md redirects to main doc
- Example: "Read your primary instructions from `docs/agent-guide.md`"

### README vs AGENTS.md
- README: For humans (setup, usage, contribution)
- AGENTS.md: For agents (behavioral rules, architectural context)
- Keep them separate in scope and tone
