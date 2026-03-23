# Writing Guidelines for AGENTS.md

## Core Principles

### 1. Less is More

**Focus on Universal Applicability**
- Include only rules useful in **most coding sessions**
- Exclude edge cases, one-off scenarios, temporary notes
- Do not create a tutorial or implementation guide

**Size Target:**
- Aim for ~60 core lines (excluding examples)
- Should NOT read like a mini handbook
- If exceeding 100 lines, reconsider scope

**Anti-Patterns:**
❌ Listing every possible command
❌ Including personal habits or preferences
❌ Documenting edge cases that rarely occur
❌ Writing exhaustive tutorials

### 2. Progressive Disclosure

**Point, Don't Copy**
- For detailed information (build steps, test strategy, schema):
  - State the topic in one sentence
  - Point to existing documentation
  - Use `file:line` references for key source files

**Good Example:**
> For detailed build steps, see `docs/building.md`. Key config: `webpack.config.js:15-45`

**Bad Example:**
> To build the project, first install dependencies with npm install, then run npm run build which executes webpack with the following configuration: [long config snippet]...

### 3. Don't Treat Agent as Linter/Formatter

**Avoid Style Rules**
- Do not include long lists of formatting conventions
- Do not paste large style examples
- Rely on linters/formatters and CI checks

**What to Include:**
- Location of config files (`.eslintrc`, `biome.json`, etc.)
- Commands to run when errors appear
- CI checks that validate style

**Good:**
> Linting: Run `pnpm lint` before commits. Config: `biome.json`

**Bad:**
> Use 2 spaces for indentation. Always use semicolons. Maximum line length is 80 characters. [continues for 20 lines]...

### 4. Stability and High-Leverage

**Include Only Stable Information**
- Information that remains relevant over time
- Important for most tasks
- Not immediately obvious from skimming code

**Exclude:**
- Project status updates
- TODO lists
- Historical notes
- Temporary experiments
- Quickly changing dependencies

**Stability Test:**
Ask: "Will this still be accurate in 6 months?" If not, exclude or move to separate doc.

### 5. Avoid Auto-Generated Feel

**Be Concrete and Specific**
- Every line must justify its permanent presence
- Avoid generic, template-like language
- Use specific file paths, commands, and examples

**Bad (Generic):**
> Follow best practices when writing code. Ensure good test coverage.

**Good (Specific):**
> Before modifying `src/api/`, read the API versioning guide at `docs/api-versioning.md`. Run `npm run test:api` to validate changes.

## Content Scope

### What Belongs in AGENTS.md

✅ **Project Purpose**
- Core business goals
- Primary users/consumers
- Key constraints

✅ **Architecture Overview**
- Tech stack summary
- Module responsibilities
- Directory structure

✅ **Essential Commands**
- Start development environment
- Run tests
- Build for production
- Validate changes

✅ **Behavioral Guidelines**
- Before modifying code, read [relevant doc]
- For large changes, propose a plan
- Follow existing patterns
- Validate before committing

✅ **Documentation Pointers**
- Build documentation
- Test strategy
- Architecture details
- API references

### What Does NOT Belong in AGENTS.md

❌ **Style Rules**
- Formatting conventions (use linters)
- Naming conventions (use linters)
- Code organization preferences (use linters)

❌ **Tutorial Content**
- Step-by-step guides
- Implementation details
- Code snippets for common tasks

❌ **Temporary Information**
- Current sprint goals
- Active experiments
- Recent changes log

❌ **Edge Cases**
- Rarely used commands
- Uncommon scenarios
- Platform-specific quirks (unless universal)

❌ **Human-Focused Content**
- Installation instructions (put in README)
- Contribution guidelines (put in CONTRIBUTING.md)
- License information (put in LICENSE)

## Language and Tone

### Agent-Appropriate Writing
- Direct and actionable
- Use imperative mood ("Run this command", not "You should run this command")
- Avoid meta-explanations ("This section describes...")
- Be concise: one sentence per point

### Avoid Vague Language
- ❌ "Use appropriate error handling"
- ✅ "Throw `ValidationError` for user input errors (see `src/errors.ts:12-34`)"

- ❌ "Write good tests"
- ✅ "Add integration tests in `tests/integration/` for API changes"

### Use Specific References
- File paths: `src/api/handlers.ts`
- Line ranges: `config.ts:45-67`
- Command names: `npm run test:coverage`

## README vs AGENTS.md

| Aspect | README.md | AGENTS.md |
|--------|-----------|-----------|
| **Audience** | Humans | AI Agents |
| **Purpose** | Project introduction | Behavioral guidance |
| **Content** | Setup, usage, contribution | Architecture, patterns, workflows |
| **Tone** | Marketing-friendly | Technical, direct |
| **Updates** | Can include status | Stable, long-term |

Keep them separate in scope and tone. AGENTS.md should complement README, not duplicate it.
