# Quality Checklist for AGENTS.md

Use this checklist to validate generated AGENTS.md files before finalizing.

## Structural Completeness

- [ ] **Project Purpose** section exists with 2-3 sentences
- [ ] **Tech Stack and Architecture** section lists main technologies
- [ ] **How to Work** section includes essential commands
- [ ] **Task-Specific Documentation** section points to relevant docs
- [ ] **Working Guidelines** section has 3-7 high-leverage rules

## Content Quality

### Project Purpose (WHY)
- [ ] Captures core business/technical goals
- [ ] Identifies primary users/consumers
- [ ] States key constraints
- [ ] Avoids generic descriptions
- [ ] Stays within 2-3 sentences

### Tech Stack and Architecture (WHAT)
- [ ] Lists languages/frameworks with versions
- [ ] Describes directory structure
- [ ] Each directory has one-sentence description
- [ ] Highlights key modules and responsibilities
- [ ] Avoids implementation details

### How to Work (HOW)
- [ ] Includes only 1-3 most important commands per subsection
- [ ] Specifies working directory if non-standard
- [ ] Mentions test/build commands
- [ ] States validation requirements
- [ ] Points to detailed docs instead of inlining

### Task-Specific Documentation
- [ ] Lists relevant documentation files
- [ ] Each entry has one-line purpose description
- [ ] Uses relative paths from project root
- [ ] Prioritizes frequently needed docs
- [ ] Avoids creating new docs if existing ones work

### Working Guidelines
- [ ] Contains 3-7 rules (not fewer, not more)
- [ ] Rules are high-leverage (apply to most sessions)
- [ ] Rules are actionable and specific
- [ ] Avoids style/formatting rules
- [ ] Includes file references where relevant

## Progressive Disclosure

- [ ] Uses pointers instead of copying large content
- [ ] References existing documentation for details
- [ ] Includes `file:line` references for key sources
- [ ] Does not inline long code snippets
- [ ] States topics in one sentence before pointing

## Stability and Relevance

- [ ] Contains only stable information
- [ ] No temporary status or TODO lists
- [ ] No historical notes or change logs
- [ ] Information will remain accurate over time
- [ ] Rules apply to most coding sessions

## Conciseness

- [ ] Document is ~60 core lines (excluding examples)
- [ ] Does not read like a tutorial or handbook
- [ ] Every line justifies its presence
- [ ] No verbose or generic language
- [ ] Avoids "auto-generated" feel

## Actionability

- [ ] Commands are specific and runnable
- [ ] File paths are accurate
- [ ] References are verifiable
- [ ] Guidelines can be followed immediately
- [ ] No vague instructions

## Scope Appropriateness

### Included (Should be there)
- [ ] Project purpose and constraints
- [ ] Tech stack overview
- [ ] Essential commands
- [ ] Behavioral guidelines
- [ ] Documentation pointers

### Excluded (Should NOT be there)
- [ ] Style/formatting rules (should use linters)
- [ ] Tutorial content (should be in separate docs)
- [ ] Temporary information (status, TODOs, history)
- [ ] Edge cases and rare scenarios
- [ ] Human-focused content (setup instructions, etc.)

## Agent-Appropriate Design

- [ ] Written for AI agents, not humans
- [ ] Uses imperative mood
- [ ] Direct and concise
- [ ] Avoids meta-explanations
- [ ] Complements README (doesn't duplicate)

## Validation Questions

Ask these questions to validate each section:

1. **Project Purpose**: Can an agent understand WHY this project exists in 10 seconds?
2. **Architecture**: Can an agent navigate the codebase with this overview?
3. **Commands**: Are the 1-3 most critical commands listed?
4. **Guidelines**: Will these rules improve agent behavior in most sessions?
5. **Pointers**: Do references point to existing, accurate documentation?

## Common Issues to Fix

### Issue: Document Too Long (>100 lines)
**Fix**: Remove tutorial content, move details to separate docs, use pointers

### Issue: Generic or Vague Language
**Fix**: Add specific file paths, commands, and examples

### Issue: Style Rules Included
**Fix**: Remove and point to linter config files instead

### Issue: Missing Essential Commands
**Fix**: Add the 1-3 most important commands for dev/test/build

### Issue: Outdated or Temporary Information
**Fix**: Remove status updates, TODOs, historical notes

### Issue: Duplicates README Content
**Fix**: Focus on agent-specific guidance, complement README

## Final Checks

- [ ] All file paths exist and are accurate
- [ ] All commands are runnable
- [ ] All documentation references exist
- [ ] No broken or placeholder references
- [ ] Content is stable and will remain relevant
- [ ] Document is in English (or project's primary language)
