#!/usr/bin/env python3
"""
Sync _data/topics.yml problem lists with .md files on disk.

Adds missing entries and removes stale ones while preserving existing labels
and topic structure. Run after adding or renaming problem files:

    python scripts/generate_question_indexes.py
    python scripts/sync_topics_yml.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from urllib.parse import quote, unquote

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    raise

REPO_ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_ROOT = REPO_ROOT / "src" / "questions"
TOPICS_YML = REPO_ROOT / "_data" / "topics.yml"


def readme_path_to_folder(readme_html: str) -> Path:
    """/src/questions/math/README.html -> src/questions/math"""
    if readme_html == "/src/questions/README.html":
        return QUESTIONS_ROOT
    rel = readme_html.removeprefix("/src/questions/").removesuffix("/README.html")
    return QUESTIONS_ROOT / rel


def md_to_html_path(folder: Path, filename: str) -> tuple[str, str]:
    base = filename[: -len(".md")]
    rel = folder.relative_to(QUESTIONS_ROOT)
    encoded = quote(base, safe="")
    parts = "/".join(rel.parts)
    html = f"/src/questions/{parts}/{encoded}.html" if parts else f"/src/questions/{encoded}.html"
    return base, html


def collect_disk_problems(folder: Path) -> dict[str, str]:
    """Map html path -> label for non-README .md files in folder."""
    out: dict[str, str] = {}
    if not folder.is_dir():
        return out
    for f in sorted(os.listdir(folder)):
        if f.lower().endswith(".md") and f != "README.md":
            label, html = md_to_html_path(folder, f)
            out[html] = label
    return out


def sync_problems(entry: dict) -> tuple[int, int]:
    """Sync entry['problems'] with disk. Returns (added, removed) counts."""
    if entry["path"] == "/src/questions/README.html":
        return 0, 0

    folder = readme_path_to_folder(entry["path"])
    disk = collect_disk_problems(folder)
    existing = {p["path"]: p for p in entry.get("problems", []) or []}
    added = removed = 0

    ordered: list[dict] = []
    for p in entry.get("problems", []) or []:
        if p["path"] in disk:
            ordered.append({"label": p["label"], "path": p["path"]})
        else:
            removed += 1

    seen = {p["path"] for p in ordered}
    new_paths = sorted(set(disk) - seen)
    for path in new_paths:
        ordered.append({"label": disk[path], "path": path})
        added += 1

    if ordered:
        entry["problems"] = ordered
    else:
        entry.pop("problems", None)

    return added, removed


def walk_and_sync(topics: list[dict]) -> tuple[int, int]:
    total_added = total_removed = 0
    for entry in topics:
        a, r = sync_problems(entry)
        total_added += a
        total_removed += r
        for child in entry.get("children", []) or []:
            ca, cr = walk_and_sync([child])
            total_added += ca
            total_removed += cr
    return total_added, total_removed


def dump_topics(topics: list[dict]) -> str:
    """Write YAML matching the hand-maintained style in topics.yml."""
    lines: list[str] = []

    def dump_problems(problems: list[dict], indent: int) -> None:
        pad = " " * indent
        lines.append(f"{pad}problems:")
        for p in problems:
            lines.append(f'{pad}  - label: "{p["label"]}"')
            lines.append(f'{pad}    path: "{p["path"]}"')

    def dump_entry(entry: dict, indent: int = 0) -> None:
        pad = " " * indent
        lines.append(f'{pad}- label: "{entry["label"]}"')
        lines.append(f'{pad}  path: "{entry["path"]}"')
        if "problems" in entry:
            dump_problems(entry["problems"], indent + 2)
        if "children" in entry:
            lines.append(f"{pad}  children:")
            for child in entry["children"]:
                cp = " " * (indent + 4)
                lines.append(f'{cp}- label: "{child["label"]}"')
                lines.append(f'{cp}  path: "{child["path"]}"')
                if "problems" in child:
                    dump_problems(child["problems"], indent + 6)

    for entry in topics:
        dump_entry(entry)

    return "\n".join(lines) + "\n"


def main() -> None:
    if not TOPICS_YML.is_file():
        raise SystemExit(f"Missing {TOPICS_YML}")

    with open(TOPICS_YML, encoding="utf-8") as f:
        topics = yaml.safe_load(f)

    added, removed = walk_and_sync(topics)

    TOPICS_YML.write_text(dump_topics(topics), encoding="utf-8")
    print(f"Synced {TOPICS_YML.relative_to(REPO_ROOT)}: +{added} added, -{removed} removed")


if __name__ == "__main__":
    main()
