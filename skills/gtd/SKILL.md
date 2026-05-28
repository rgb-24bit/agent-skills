---
name: gtd
description: Personal task management system. Use when users want to manage tasks, track work items, list tasks, create subtasks, mark tasks done, check what to do next, or update task context. Handles agent-executed tasks, ad-hoc interrupts, and planned work items. Triggers on commands /gtd or gtd with subcommands add, list, show, start, done, block, cancel, subtask, next, context, edit.
---

# GTD — Personal Task Management

The user manages three types of work across constant context switching: agent-delegated tasks, ad-hoc interrupts, and planned work items. The GTD system stores tasks as Markdown files with YAML frontmatter and provides a CRUD script for file operations. The agent's job is to understand the user's natural language intent and translate it into script calls.

## Storage Model

```
~/.gtd/
├── 20260528T093000.md    # active tasks (status ≠ done/cancelled)
├── 20260529T110000.md
└── archive/
    └── ...               # done and cancelled tasks
```

Each task file:

```markdown
---
type: planned
title: 重构 auth 模块 token 刷新逻辑
status: todo
deadline: 2026-06-05
tags: [backend, tech-debt]
---

Free-form body text. The agent manages this section — reading old content,
synthesizing with new user input, and writing back a coherent updated version.
This is NOT a timestamped log. It is the task's full current context.
```

| Field    | Required | Values                                           |
|----------|----------|--------------------------------------------------|
| `type`   | yes      | `agent` / `ad-hoc` / `planned`                   |
| `title`  | yes      | Free text, used for fuzzy matching               |
| `status` | yes      | `todo` / `in-progress` / `blocked` / `done` / `cancelled` |
| `deadline` | no     | `YYYY-MM-DD`                                     |
| `tags`   | no       | YAML list, free-form                             |

If `~/.gtd/` does not exist, create it (and `archive/`) automatically.

## Agent Interaction Pattern

The user types `/gtd` followed by natural language. The agent:

1. **Infer the action** — what does the user want to do? (create, start, block, complete, cancel, check progress, etc.)
2. **Find the target task** — if the action targets an existing task, run `gtd list` first to see candidates, then fuzzy-match the title. If ambiguous, present options to the user.
3. **Read current state** — if the body needs updating, run `gtd show "title"` to get the full body first.
4. **Synthesize the body** — combine the old body with the user's new input into a coherent updated body. Write it back via `--body`.
5. **Execute the action** — call the appropriate script command with the correct flags.

### Principles for Body Synthesis

`--body` does a **full replacement**, not an append. The agent MUST:

- Read the old body first (`gtd show`)
- Understand what the user is saying now — new progress, decisions, blockers, results
- Rewrite the body to reflect the current state of the task, incorporating both old context and new input
- Not produce timestamped log entries. The body is a living document, not a journal.
- Keep it concise and useful for context recovery when the user comes back to this task later

If the user says "开始做了，先读代码", the body should say something meaningful about what phase the task is in, not "2026-05-29T10:00 — 开始做了"。

If the user provides no new body information (just a status change), leave the body as-is.

### Title Matching

- Always run `gtd list` first to see available tasks
- Fuzzy-match the user's words against task titles
- If one task is clearly intended, use its exact title
- If multiple tasks match, show the user the candidates and ask which one
- Only active tasks are searched (not archive)

## Action Inference

Map the user's natural language to one of the script commands. Look for intent, not keywords. The user may express the same action in many ways.

**Create a task** → `gtd add "title" --type <type> [--deadline ...] [--tags ...] [--body "..."]`
- "加一个重构 auth 的任务，属于 planned"
- "新建：修登录 bug，ad-hoc 的，deadline 是周五"
- "记录一下，oncall 的 502 排查"
- Infer `--type` from context: agent tasks are things delegated to AI, ad-hoc are interrupts/requests, planned are formal dev work
- If type isn't clear, ask

**Start a task** → `gtd start "title" [--body "..."]`
- "开始做重构 auth"
- "着手处理登录 bug"
- "搞一下 502 排查"
- Usually the user provides context about what they're about to do — capture that in the body

**Complete a task** → `gtd done "title" [--body "..."]`
- "重构 auth 做完了"
- "登录 bug 修好了，根因是..."
- "502 那个搞定了"
- The user often provides closing notes — capture them in the body before archiving

**Block a task** → `gtd block "title" [--body "..."]`
- "重构 auth 被阻塞了，等后端给 API"
- "登录 bug 卡住了"
- The body should explain what's blocking and what needs to happen to unblock

**Cancel a task** → `gtd cancel "title" [--body "..."]`
- "重构 auth 不做了，需求取消了"
- "502 排查不用搞了"

**Edit metadata** → `gtd edit "title" [--deadline ...] [--tags ...] [--title ...] [--type ...] [--body "..."]`
- "重构 auth 的 deadline 改成下周"
- "给登录 bug 加个 frontend 标签"
- "把 502 的标题改成 502 根因分析"
- Only include flags that actually change

**Check what to do next** → `gtd next`
- "现在该干啥"
- "有什么任务"
- "接下来做什么"
- No further action needed — just run and display results

**View task details** → `gtd show "title"`
- "看一下重构 auth 的详情"

**List tasks** → `gtd list [--status ...] [--type ...]`
- "列一下所有任务"
- "有哪些 planned 的任务"
- "被阻塞的任务有哪些"

## Script Reference

The script at `scripts/gtd.py` provides these commands. The agent calls them via Bash.

```
gtd add "title" --type agent|ad-hoc|planned [--deadline YYYY-MM-DD] [--tags t1,t2] [--body "..."]
gtd list [--status todo|in-progress|blocked] [--type agent|ad-hoc|planned] [--tag tag]
gtd show "title"                                    # fuzzy match, prints frontmatter + body
gtd start "title" [--body "..."]                    # status → in-progress, optional body replacement
gtd done "title" [--body "..."]                     # status → done, archive, optional body replacement
gtd block "title" [--body "..."]                    # status → blocked, optional body replacement
gtd cancel "title" [--body "..."]                   # status → cancelled, archive, optional body replacement
gtd edit "title" [--deadline ...] [--tags ...] [--title ...] [--type ...] [--body "..."]
gtd next                                             # three-tier recommendation
```

All `--body` flags do full replacement. `--tags` accepts comma-separated values. `--deadline` accepts `YYYY-MM-DD`.

`gtd list`, `gtd show`, and `gtd next` are read-only and safe to run without user approval. Write commands (`add`, `start`, `done`, `block`, `cancel`, `edit`) modify files and should be confirmed with the user if the matching is ambiguous.

## Examples

**Creating and starting work:**

```
User: /gtd 加一个重构 auth 的任务，planned 类型，deadline 是 6 月 5 号
Agent: [calls: gtd add "重构 auth" --type planned --deadline 2026-06-05]
→ Created.

User: /gtd 开始做重构 auth，先梳理现有 token 刷新流程
Agent: [calls: gtd start "重构 auth" --body "### 当前阶段\n梳理现有 token 刷新流程，了解当前实现。"]
→ Started.
```

**Completing a task with closing notes:**

```
User: /gtd 重构 auth 做完了，根因是 refresh token 和 access token 的并发更新
      导致竞态条件，改成了串行队列处理
Agent: [calls: gtd show "重构 auth" → reads old body]
       [synthesizes: old progress notes + closing summary]
       [calls: gtd done "重构 auth" --body "### 当前阶段\n已完成。\n\n### 结论\n根因是 refresh token 和 access token 的并发更新导致竞态条件。修复方案：改为串行队列处理。"]
→ Done and archived.
```

**Blocking:**

```
User: /gtd 重构 auth 卡住了，等后端给新 API，已经催了两次
Agent: [calls: gtd show "重构 auth" → reads old body]
       [synthesizes: old progress + block reason]
       [calls: gtd block "重构 auth" --body "### 当前阶段\n阻塞中。\n\n### 阻塞原因\n等待后端提供新的 token 验证 API，已催两次。解除后继续。"]
→ Blocked.
```

**Checking what to do:**

```
User: /gtd 现在该干啥
Agent: [calls: gtd next]
       → Tier 1: Agent task "重构 auth" is running — check its progress.
       → Tier 2: Ad-hoc: 帮小王看部署问题 (due 05-29)
       → Tier 3: Planned: 更新 CI 流水线 (related to recent work)
```
