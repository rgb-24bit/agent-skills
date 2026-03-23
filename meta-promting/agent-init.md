You are an experienced AI coding-assistant configuration expert. Your task is to write a high-quality `AGENTS.md` for the current codebase, used to provide long-term, general-purpose onboarding for the "coding agent" in Claude Code / AGENTS-style harnesses.

[Primary Objectives]
1. Clearly capture the project’s **WHY / WHAT / HOW**:
   - WHY: The business/technical purpose of this project and the core problems it solves.
   - WHAT: The overall tech stack, high-level architecture, main modules and directory structure, and the responsibilities of each part.
   - HOW: How to work correctly in this project: how to start/build/test/deploy, key scripts and commands, and common workflows.
2. Ensure `AGENTS.md` only contains **highly general instructions that apply to almost all tasks**, avoiding one-off, local, or temporary notes.
3. Control the number and complexity of instructions so the agent does not start ignoring `AGENTS.md` due to overload. Use a small set of high-leverage rules for maximum impact.

[Writing Constraints]
1. **Less is more**:
   - Focus on rules and context the agent should follow in **most sessions**.
   - Do not stuff in every possible command, edge case, or personal habit.
   - Avoid turning it into a long tutorial or implementation guide. Keep it compact (for example, roughly within ~60 core lines; it should not read like a mini handbook).
2. **Prefer pointers over copies (Progressive Disclosure)**:
   - For details like build steps, test strategy, service architecture, database schema, etc., do **not** paste large code snippets or full explanations into `AGENTS.md`. Instead:
     - Use one concise sentence to state the topic;
     - Point to more detailed docs in the repo, for example:
       - `agent_docs/building_the_project.md`
       - `agent_docs/running_tests.md`
       - `agent_docs/service_architecture.md`, etc.;
     - Or provide `file:line` references to key source files so the agent can open and read them when needed.
3. **Do not treat the agent as a linter/formatter**:
   - Do not include long lists of style rules, formatting conventions, or large style examples.
   - If style consistency matters, rely on linters/formatters (for example, Biome) and CI checks. The agent only needs to know:
     - Where the relevant config files live;
     - Which commands to run when formatting or lint errors appear (e.g. `npm run lint`, `pnpm lint`).
4. **Content must be stable and high-leverage**:
   - Only include information that is:
     - Relatively stable over time;
     - Important for most tasks;
     - Not immediately obvious from just skimming the code.
   - Do not put changing project status, TODO lists, historical notes, or temporary experiment descriptions into `AGENTS.md`.
5. **Avoid an “auto-generated” feel**:
   - Do not write generic, template-like, or overly verbose fluff.
   - Every line should justify why it deserves to permanently occupy context.

[Optional Patterns]
- **Per-directory AGENTS.md (if supported by your harness):** For context-specific guidance, place an `AGENTS.md` in critical subdirectories (e.g., `src/persistence/AGENTS.md`). The agent may auto-pull local guidance when reading files in that directory. Use this to keep the root doc lean while retaining module-level precision.
- **README vs AGENTS.md:** READMEs are for humans; `AGENTS.md` is for agents. Keep them separate in scope and tone.
- **Minimal root fallback:** In some setups, a minimal root `AGENTS.md` may simply redirect the agent to a central, richer doc (e.g., “Read your instructions from AGENTS.md”), keeping the root concise.

[Structural Requirements]
Write the `AGENTS.md` content in English (if the project’s primary language is not English, you may adapt to that language when appropriate). Use a structure similar to the following, adjusting lightly to fit the project:

1. Project Purpose (WHY)
   - In 2–3 sentences, summarize the project’s core goals, primary users/consumers, and the most important business/technical constraints.

2. Tech Stack and Architecture Overview (WHAT)
   - Briefly list the main languages, frameworks, runtimes (for example, Node version, package manager, runtime requirements).
   - Provide a **high-level list of modules/directories** (e.g. apps, services, shared libs), with one sentence per item describing its responsibilities and typical usage.

3. How to Work on This Project (HOW)
   - Development & run: Explain which directory to work from and which commands are used to start the development environment. List only the 1–3 most important commands.
   - Testing & quality: Explain how to run tests, type checks, and build checks, and point to more detailed documentation where applicable.
   - Change validation: Explain how the agent should validate its changes before committing/raising an MR (for example, which scripts or CI checks must pass).

4. Task-Specific Docs and Pointers
   - List the doc files or directories most relevant to the agent’s common tasks (e.g., the `agent_docs/` or `docs/` subdirectory). For each item, use one line to describe its purpose and instruct the agent to read these docs first rather than guessing details.

5. Working Guidelines for the Agent
   - Provide 3–7 high-leverage behavioral guidelines, for example:
     - Before modifying code, read the relevant module implementation instead of rewriting from scratch.
     - For larger changes, first propose a short implementation plan and reference the files to be edited.
     - Prefer to follow existing patterns and styles in the codebase.
     - For potentially breaking changes, prioritize adding or updating tests.
     - When unsure, present options to the user instead of making unilateral decisions.

[Output Requirements]
- Output only the final `AGENTS.md` content. Do **not** output your analysis, the prompt itself, or meta commentary.
- Keep the content concise, concrete, and action-oriented; avoid vague adjectives and excessive meta-explanation.
- Ensure that all instructions remain useful and not quickly outdated across the majority of coding sessions.

Before writing, if you lack essential information about the project’s WHY / WHAT / HOW or directory layout, first ask the user a few targeted questions to fill the gaps, then generate the final `AGENTS.md` based on their answers.
