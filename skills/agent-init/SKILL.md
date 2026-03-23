---
name: agent-init
description: Generate AGENTS.md documentation for codebases to guide Code Agent behavior; use when initializing AI coding assistant configurations, standardizing agent behavior, or creating agent guidance docs for new projects
---

# Agent Initialization - AGENTS.md Generator

## Task Objective
- Generate a high-quality `AGENTS.md` file that provides long-term, general-purpose onboarding for coding agents
- Capture the project's **WHY / WHAT / HOW** framework concisely
- Ensure guidelines are stable, high-leverage, and applicable to most coding sessions

## Prerequisites
- Read the project's key configuration files (package.json, requirements.txt, Cargo.toml, etc.)
- Identify the project's primary language and tech stack
- Understand the directory structure and main modules
- Locate existing documentation (README.md, docs/, etc.)

## Operation Steps

### Step 1: Project Analysis
Analyze the codebase to extract:

**WHY (Purpose)**
- Core business/technical goals
- Primary users/consumers
- Key constraints (business, technical, regulatory)

**WHAT (Architecture)**
- Main languages, frameworks, runtimes
- High-level directory structure and module responsibilities
- Key dependencies and their purposes

**HOW (Workflow)**
- Development environment setup
- Build/test/deploy commands
- Common workflows and validation steps

**Analysis Techniques:**
- Read package manager files to identify dependencies and scripts
- Examine directory structure to understand module organization
- Check for existing documentation (README.md, CONTRIBUTING.md, docs/)
- Identify configuration files for linters, formatters, CI/CD

### Step 2: Generate AGENTS.md
Use the template from [references/agents-md-template.md](references/agents-md-template.md) to structure the document:

1. **Project Purpose**: 2-3 sentences capturing core goals and constraints
2. **Tech Stack and Architecture**: Brief list with directory/module responsibilities
3. **How to Work**: Essential commands and validation steps
4. **Task-Specific Docs**: Pointers to detailed documentation
5. **Working Guidelines**: 3-7 high-leverage behavioral rules

**Critical Principles:**
- Follow the writing guidelines in [references/writing-guidelines.md](references/writing-guidelines.md)
- Keep it compact (~60 core lines, not a handbook)
- Use pointers over copies (progressive disclosure)
- Avoid linter/formatter details - point to config files instead
- Every line must justify its permanent presence

### Step 3: Quality Validation
Validate against the checklist in [references/quality-checklist.md](references/quality-checklist.md):

- Content stability and relevance
- Progressive disclosure implementation
- Actionability and specificity
- Appropriate scope (general vs. specific)

### Step 4: Information Gap Handling
If essential information is missing:
- Ask the user 2-4 targeted questions
- Focus on WHY/WANT/HOW gaps
- Do not generate incomplete or generic content

## Resource Index
- **Template**: [references/agents-md-template.md](references/agents-md-template.md) - Standard structure for AGENTS.md
- **Writing Guidelines**: [references/writing-guidelines.md](references/writing-guidelines.md) - Constraints and best practices
- **Quality Checklist**: [references/quality-checklist.md](references/quality-checklist.md) - Validation criteria

## Critical Guidelines

**Less is More**
- Focus on rules applicable in **most sessions**
- Avoid edge cases, one-off notes, temporary information
- Do not turn AGENTS.md into a tutorial or implementation guide

**Progressive Disclosure**
- For details (build steps, test strategy, schema), point to existing docs
- Use file:line references for key source files
- Example: "See `agent_docs/building_the_project.md` for build details"

**Stability Over Completeness**
- Only include stable, high-leverage information
- Exclude changing status, TODO lists, historical notes
- Prefer pointers to detailed documentation over inlining content

**Agent-Appropriate Scope**
- AGENTS.md is for agents; README is for humans
- Do not include style rules (rely on linters/formatters)
- Provide commands to run when lint/format errors appear

**High-Leverage Guidelines**
- Before modifying code, read relevant module implementation
- For larger changes, propose a plan and reference files to edit
- Follow existing patterns and styles in the codebase
- For breaking changes, prioritize adding/updating tests
- When unsure, present options instead of unilateral decisions

## Usage Example

**Scenario**: User requests AGENTS.md for a Node.js/TypeScript project

**Execution Flow**:
1. Read package.json to identify dependencies and scripts
2. Examine directory structure (src/, tests/, docs/, etc.)
3. Check for existing documentation
4. Identify tech stack (Node version, package manager, frameworks)
5. Generate AGENTS.md following template structure
6. Validate against quality checklist
7. If gaps exist, ask targeted questions

**Key Outputs**:
- Concise project purpose statement
- Tech stack overview with module responsibilities
- 1-3 essential commands for dev/test/build
- Pointers to detailed documentation
- 3-7 high-leverage behavioral guidelines
