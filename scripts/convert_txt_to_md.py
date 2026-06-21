#!/usr/bin/env python3
"""Convert .txt question notes to .md (formatting only, no new content)."""

from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from format_md_questions import (  # noqa: E402
    is_cpp_preprocessor,
    is_likely_code_line,
    title_from_path,
)


def is_section_header(line: str) -> bool:
    s = line.strip()
    if re.match(r"^Steps:\s*$", s):
        return True
    if re.match(r"^\d+\)\s*$", s):
        return True
    if re.match(r"^\d+\)\s+[A-Z]", s):
        return True
    if re.match(r"^\d+\)[A-Z][a-z]{7,}", s):
        return True
    return False


def is_definitely_code(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s in ("{", "}", "else", "else{"):
        return True
    if s.endswith(";") or s.endswith("{") or s.endswith("}"):
        return True
    if is_cpp_preprocessor(s):
        return True
    if re.match(r"^[a-zA-Z_]\w*\.", s):
        return True
    if re.match(r"^arr\s*=", s):
        return True
    if re.match(
        r"^(m\[|s\[|arr\[|v\[|cout|cin|for\s*\(|while\s*\(|if\s*\(|return\s|vector|map|set|pair|priority_queue|string\s)",
        s,
    ):
        return True
    if ";" in s:
        tail = s.rsplit(";", 1)[1].strip()
        if not tail or tail.startswith("//") or tail.startswith("...") or tail.startswith(".."):
            return True
    return False


def classify_line(line: str) -> str:
    s = line.strip()
    if not s:
        return "blank"
    if is_section_header(line):
        return "section"
    if re.match(r"^\d+\)", s):
        if re.match(r"^\d+\)\s*(int|ll|string|void|bool|#include)", s):
            return "code"
        return "prose"
    if "=>" in s:
        return "prose"
    if s.startswith("#") and not is_cpp_preprocessor(s):
        return "prose"
    if is_definitely_code(line) or is_likely_code_line(line):
        return "code"
    return "prose"


def emit_prose(lines: list[str], out: list[str]) -> None:
    if not lines:
        return
    text = "\n".join(lines).rstrip()
    if text:
        out.append(text)
        out.append("")


def emit_code(lines: list[str], out: list[str]) -> None:
    if not lines:
        return
    body = "\n".join(lines).rstrip("\n")
    out.append("```cpp")
    out.append(body)
    out.append("```")
    out.append("")


def convert_content(content: str, path: str) -> str:
    title = title_from_path(path)
    raw = content.replace("\r\n", "\n").rstrip("\n")
    if not raw.strip():
        return f"# {title}\n"

    lines = raw.split("\n")
    out: list[str] = [f"# {title}", ""]
    prose_buf: list[str] = []
    code_buf: list[str] = []
    current: str | None = None

    def flush() -> None:
        nonlocal current
        if current == "prose":
            emit_prose(prose_buf, out)
            prose_buf.clear()
        elif current == "code":
            emit_code(code_buf, out)
            code_buf.clear()
        current = None

    for line in lines:
        kind = classify_line(line)
        if kind == "blank":
            if current == "code":
                code_buf.append("")
            elif current == "prose":
                flush()
            continue
        if kind == "section":
            flush()
            out.append(f"## {line.rstrip()}")
            out.append("")
            continue
        if kind == "prose":
            if current == "code":
                flush()
            current = "prose"
            prose_buf.append(line.rstrip())
        else:
            if current == "prose":
                flush()
            current = "code"
            code_buf.append(line.rstrip())

    flush()
    return "\n".join(out).rstrip() + "\n"


def convert_file(txt_path: str, delete_txt: bool = False) -> tuple[bool, str]:
    md_path = txt_path[:-4] + ".md"
    try:
        with open(txt_path, encoding="utf-8", errors="strict") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(txt_path, encoding="utf-8", errors="replace") as f:
            content = f.read()

    new_content = convert_content(content, md_path)
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)

    if delete_txt:
        os.remove(txt_path)

    return True, md_path


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: convert_txt_to_md.py <directory> [--delete-txt]", file=sys.stderr)
        sys.exit(1)

    target = os.path.abspath(sys.argv[1])
    delete_txt = "--delete-txt" in sys.argv

    if not os.path.isdir(target):
        print("Not a directory:", target, file=sys.stderr)
        sys.exit(1)

    converted = 0
    for name in sorted(os.listdir(target)):
        if not name.endswith(".txt"):
            continue
        txt_path = os.path.join(target, name)
        convert_file(txt_path, delete_txt=delete_txt)
        converted += 1
        print(f"  CONVERTED: {name} -> {name[:-4]}.md")

    print(f"\nConverted {converted} file(s) in {target}")

    if converted:
        import format_md_questions as fmt

        updated = 0
        for name in sorted(os.listdir(target)):
            if not name.endswith(".md"):
                continue
            path = os.path.join(target, name)
            changed, _ = fmt.process_file(path)
            if changed:
                updated += 1
                print(f"  FORMATTED: {name}")
        print(f"Post-format pass: {updated} file(s) updated")


if __name__ == "__main__":
    main()
