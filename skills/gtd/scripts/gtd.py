#!/usr/bin/env python3
"""GTD task management — file I/O handler for the gtd skill.

Pure CRUD layer: create, read, update frontmatter, move to archive.
Agent handles natural language understanding and body synthesis.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from difflib import SequenceMatcher
from typing import Optional

GTD_DIR = Path.home() / ".gtd"
ARCHIVE_DIR = GTD_DIR / "archive"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def ensure_dirs():
    GTD_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)


def parse_frontmatter(filepath: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text) from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).strip().split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",") if v.strip()]
            else:
                val = val.strip('"').strip("'")
            fm[key] = val
    body = text[m.end():].strip()
    return fm, body


def write_frontmatter(filepath: Path, fm: dict, body: str):
    """Write a task file with frontmatter + body."""
    lines = ["---"]
    field_order = ["type", "title", "status", "deadline", "tags"]
    for key in field_order:
        if key in fm:
            val = fm[key]
            if isinstance(val, list):
                val_str = "[" + ", ".join(val) + "]"
            else:
                val_str = str(val)
            lines.append(f"{key}: {val_str}")
    for key in fm:
        if key not in field_order:
            val = fm[key]
            if isinstance(val, list):
                val_str = "[" + ", ".join(val) + "]"
            else:
                val_str = str(val)
            lines.append(f"{key}: {val_str}")
    lines.append("---")
    if body:
        lines.append("")
        lines.append(body)
    lines.append("")
    filepath.write_text("\n".join(lines), encoding="utf-8")


def active_tasks() -> list[Path]:
    """Return list of .md files in GTD_DIR (not archive)."""
    ensure_dirs()
    return sorted(GTD_DIR.glob("*.md"))


def fuzzy_match(query: str, candidates: list[Path]) -> list[tuple[Path, float]]:
    """Return candidates sorted by title similarity score (best first)."""
    scored = []
    for fp in candidates:
        fm, _ = parse_frontmatter(fp)
        title = fm.get("title", fp.stem)
        score = SequenceMatcher(None, query.lower(), title.lower()).ratio()
        if query.lower() in title.lower():
            score += 0.5
        scored.append((fp, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


def find_task(title_query: str) -> Optional[Path]:
    """Find a single active task by title. Returns None if no match or ambiguous."""
    candidates = active_tasks()
    matches = fuzzy_match(title_query, candidates)
    if not matches:
        return None
    best_score = matches[0][1]
    if best_score > 0.7 and (len(matches) == 1 or matches[1][1] < best_score - 0.15):
        return matches[0][0]
    return None


def find_task_interactive(title_query: str) -> Optional[Path]:
    """Print candidate list as JSON for the agent to resolve ambiguity."""
    candidates = active_tasks()
    matches = fuzzy_match(title_query, candidates)
    if not matches:
        print(json.dumps({"found": False, "candidates": []}, ensure_ascii=False))
        return None
    reasonable = [(fp, s) for fp, s in matches if s > 0.3]
    if not reasonable:
        print(json.dumps({"found": False, "candidates": []}, ensure_ascii=False))
        return None
    result = {
        "found": True,
        "candidates": [
            {
                "file": str(fp.name),
                "title": parse_frontmatter(fp)[0].get("title", ""),
                "status": parse_frontmatter(fp)[0].get("status", ""),
                "score": round(s, 3),
            }
            for fp, s in reasonable[:10]
        ],
    }
    print(json.dumps(result, ensure_ascii=False))
    return None


# ── Command handlers ──────────────────────────────────────────────


def cmd_add(args):
    ensure_dirs()
    now = datetime.now().strftime("%Y%m%dT%H%M%S%f")
    filepath = GTD_DIR / f"{now}.md"
    while filepath.exists():
        now = datetime.now().strftime("%Y%m%dT%H%M%S%f")
        filepath = GTD_DIR / f"{now}.md"
    fm = {"type": args.type, "title": args.title, "status": "todo"}
    if args.deadline:
        fm["deadline"] = args.deadline
    if args.tags:
        fm["tags"] = [t.strip() for t in args.tags.split(",")]
    body = args.body if args.body else ""
    write_frontmatter(filepath, fm, body)
    print(f"Created {filepath}")


def cmd_list(args):
    tasks = active_tasks()
    rows = []
    for fp in tasks:
        fm, _ = parse_frontmatter(fp)
        if args.status and fm.get("status") != args.status:
            continue
        if args.type and fm.get("type") != args.type:
            continue
        if args.tag:
            tags = fm.get("tags", [])
            if not isinstance(tags, list):
                tags = [tags]
            if args.tag not in tags:
                continue
        rows.append((fm.get("title", fp.stem), fm.get("status", ""), fm.get("type", ""), fm.get("deadline", "-")))
    if not rows:
        print("No tasks found.")
        return
    max_title = min(max(len(r[0]) for r in rows), 60)
    title_w = max(max_title, 10)
    print(f"{'Title':<{title_w}}  Status        Type      Deadline")
    print("-" * (title_w + 38))
    for title, status, typ, dl in rows:
        print(f"{title[:title_w]:<{title_w}}  {status:<12}  {typ:<8}  {dl}")


def cmd_show(args):
    fp = find_task(args.title)
    if fp is None:
        find_task_interactive(args.title)
        return
    fm, body = parse_frontmatter(fp)
    print(f"File: {fp.name}")
    print(f"Title: {fm.get('title', '')}")
    print(f"Type: {fm.get('type', '')}")
    print(f"Status: {fm.get('status', '')}")
    print(f"Deadline: {fm.get('deadline', '-')}")
    tags = fm.get("tags", [])
    if isinstance(tags, list):
        print(f"Tags: {', '.join(tags) if tags else '-'}")
    else:
        print(f"Tags: {tags}")
    print(f"Mtime: {datetime.fromtimestamp(fp.stat().st_mtime).strftime('%Y-%m-%dT%H:%M:%S')}")
    print()
    print(body if body else "(empty)")


def cmd_start(args):
    fp = find_task(args.title)
    if fp is None:
        find_task_interactive(args.title)
        return
    fm, body = parse_frontmatter(fp)
    fm["status"] = "in-progress"
    if args.body is not None:
        body = args.body
    write_frontmatter(fp, fm, body)
    print(f"Started: {fm['title']}")


def cmd_done(args):
    fp = find_task(args.title)
    if fp is None:
        find_task_interactive(args.title)
        return
    fm, body = parse_frontmatter(fp)
    fm["status"] = "done"
    if args.body is not None:
        body = args.body
    write_frontmatter(fp, fm, body)
    dest = ARCHIVE_DIR / fp.name
    fp.rename(dest)
    print(f"Done and archived: {fm['title']}")


def cmd_block(args):
    fp = find_task(args.title)
    if fp is None:
        find_task_interactive(args.title)
        return
    fm, body = parse_frontmatter(fp)
    fm["status"] = "blocked"
    if args.body is not None:
        body = args.body
    write_frontmatter(fp, fm, body)
    print(f"Blocked: {fm['title']}")


def cmd_cancel(args):
    fp = find_task(args.title)
    if fp is None:
        find_task_interactive(args.title)
        return
    fm, body = parse_frontmatter(fp)
    fm["status"] = "cancelled"
    if args.body is not None:
        body = args.body
    write_frontmatter(fp, fm, body)
    dest = ARCHIVE_DIR / fp.name
    fp.rename(dest)
    print(f"Cancelled and archived: {fm['title']}")


def cmd_next(args):
    tasks = active_tasks()
    results = {"tier1": [], "tier2": [], "tier3": []}

    for fp in tasks:
        fm, body = parse_frontmatter(fp)
        status = fm.get("status", "")
        typ = fm.get("type", "")
        mtime = fp.stat().st_mtime
        if typ == "agent" and status == "in-progress":
            results["tier1"].append({"file": fp.name, "title": fm.get("title", ""), "mtime": mtime})
    results["tier1"].sort(key=lambda x: x["mtime"], reverse=True)

    for fp in tasks:
        fm, body = parse_frontmatter(fp)
        status = fm.get("status", "")
        typ = fm.get("type", "")
        mtime = fp.stat().st_mtime
        if typ == "ad-hoc" and status in ("todo", "in-progress"):
            dl = fm.get("deadline", "")
            results["tier2"].append({
                "file": fp.name, "title": fm.get("title", ""),
                "deadline": dl, "mtime": mtime, "created": fp.stat().st_ctime,
            })

    def t2_key(x):
        return (x["deadline"] if x["deadline"] else "9999-99-99", x["created"])
    results["tier2"].sort(key=t2_key)

    now = datetime.now().timestamp()
    three_days_ago = now - 3 * 86400
    one_day_ago = now - 1 * 86400

    recent_active = []
    planned_candidates = []
    for fp in tasks:
        fm, body = parse_frontmatter(fp)
        status = fm.get("status", "")
        typ = fm.get("type", "")
        mtime = fp.stat().st_mtime
        if mtime >= one_day_ago:
            recent_active.append((fm, body))
        if typ == "planned" and status == "todo" and mtime >= three_days_ago:
            planned_candidates.append((fp, fm, body, mtime))

    if recent_active and planned_candidates:
        context_words = set()
        for fm, body in recent_active:
            for word in fm.get("title", "").lower().split():
                if len(word) > 1:
                    context_words.add(word)
            for word in body.lower().split():
                if len(word) > 2:
                    context_words.add(word)
        for fp, fm, body, mtime in planned_candidates:
            all_words = set(fm.get("title", "").lower().split())
            if body:
                all_words |= set(body.lower().split())
            overlap = len(context_words & all_words)
            results["tier3"].append({
                "file": fp.name, "title": fm.get("title", ""),
                "deadline": fm.get("deadline", ""), "mtime": mtime, "relevance": overlap,
            })
        results["tier3"].sort(key=lambda x: x["relevance"], reverse=True)
        results["tier3"] = [t for t in results["tier3"] if t["relevance"] > 0][:3]

    any_output = False

    if results["tier1"]:
        any_output = True
        print("═ Tier 1 — Agent tasks in progress (check on them)")
        for t in results["tier1"]:
            ts = datetime.fromtimestamp(t["mtime"]).strftime("%m-%d %H:%M")
            print(f"  [{t['file']}] {t['title']}  (last active: {ts})")
        print()

    if results["tier2"]:
        any_output = True
        print("═ Tier 2 — Unblocked ad-hoc tasks")
        for t in results["tier2"][:5]:
            dl = f"due {t['deadline']}" if t["deadline"] else "no deadline"
            print(f"  [{t['file']}] {t['title']}  ({dl})")
        print()

    if results["tier3"]:
        any_output = True
        print("═ Tier 3 — Context-relevant planned tasks")
        for t in results["tier3"]:
            dl = f"due {t['deadline']}" if t.get("deadline") else "no deadline"
            print(f"  [{t['file']}] {t['title']}  ({dl}, relevance: {t['relevance']})")
        print()

    if not any_output:
        print("No active tasks. Take a break or create some with gtd.")


def cmd_edit(args):
    fp = find_task(args.title)
    if fp is None:
        find_task_interactive(args.title)
        return
    fm, body = parse_frontmatter(fp)
    changed = False
    if args.deadline:
        fm["deadline"] = args.deadline
        changed = True
    if args.tags:
        fm["tags"] = [t.strip() for t in args.tags.split(",")]
        changed = True
    if args.edit_title:
        fm["title"] = args.edit_title
        changed = True
    if args.type:
        fm["type"] = args.type
        changed = True
    if args.body is not None:
        body = args.body
        changed = True
    if changed:
        write_frontmatter(fp, fm, body)
        print(f"Updated: {fm['title']}")
    else:
        print("No changes specified.")


# ── Argument parser ───────────────────────────────────────────────


def main():
    ensure_dirs()
    parser = argparse.ArgumentParser(prog="gtd", description="GTD task management - file I/O layer")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Create a task")
    p_add.add_argument("title")
    p_add.add_argument("--type", required=True, choices=["agent", "ad-hoc", "planned"])
    p_add.add_argument("--deadline")
    p_add.add_argument("--tags")
    p_add.add_argument("--body", help="Initial body text")

    p_list = sub.add_parser("list", help="List active tasks")
    p_list.add_argument("--status", choices=["todo", "in-progress", "blocked"])
    p_list.add_argument("--type", choices=["agent", "ad-hoc", "planned"])
    p_list.add_argument("--tag")

    p_show = sub.add_parser("show", help="Display task details")
    p_show.add_argument("title")

    p_start = sub.add_parser("start", help="Mark task in-progress")
    p_start.add_argument("title")
    p_start.add_argument("--body", help="Replacement body text")

    p_done = sub.add_parser("done", help="Complete and archive a task")
    p_done.add_argument("title")
    p_done.add_argument("--body", help="Replacement body text")

    p_block = sub.add_parser("block", help="Block a task")
    p_block.add_argument("title")
    p_block.add_argument("--body", help="Replacement body text")

    p_cancel = sub.add_parser("cancel", help="Cancel and archive a task")
    p_cancel.add_argument("title")
    p_cancel.add_argument("--body", help="Replacement body text")

    sub.add_parser("next", help="Recommend what to work on")

    p_edit = sub.add_parser("edit", help="Modify task metadata")
    p_edit.add_argument("title")
    p_edit.add_argument("--deadline")
    p_edit.add_argument("--tags")
    p_edit.add_argument("--title", dest="edit_title")
    p_edit.add_argument("--type", choices=["agent", "ad-hoc", "planned"])
    p_edit.add_argument("--body", help="Replacement body text")

    args = parser.parse_args()

    commands = {
        "add": cmd_add,
        "list": cmd_list,
        "show": cmd_show,
        "start": cmd_start,
        "done": cmd_done,
        "block": cmd_block,
        "cancel": cmd_cancel,
        "next": cmd_next,
        "edit": cmd_edit,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
