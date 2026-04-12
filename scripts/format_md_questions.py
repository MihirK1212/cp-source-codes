#!/usr/bin/env python3
"""
Format markdown files under src/questions: add fences/headers where missing,
fix unclosed fences, fix nested markdown links, linkify bare URLs outside
code fences. Does not remove existing content.
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "src", "questions")
ROOT = os.path.normpath(ROOT)


def title_from_path(path: str) -> str:
    base = os.path.basename(path)
    if base.lower().endswith(".md"):
        base = base[: -len(".md")]
    return base


def is_markdown_header_line(line: str) -> bool:
    return bool(re.match(r"^#{1,6}\s", line.lstrip()))


def is_cpp_preprocessor(line: str) -> bool:
    s = line.strip()
    if not s.startswith("#"):
        return False
    if re.match(r"^#{1,6}\s", s):
        return False
    return s.startswith(
        (
            "#include",
            "#define",
            "#if",
            "#ifdef",
            "#ifndef",
            "#else",
            "#elif",
            "#endif",
            "#pragma",
            "#error",
        )
    )


def is_likely_code_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if is_cpp_preprocessor(s):
        return True
    if s.startswith("//") or s.startswith("/*") or s.endswith("*/"):
        return True
    if s.startswith("using namespace"):
        return True
    if s.startswith("import ") and ("java" in s or s.startswith("import static")):
        return True
    if re.match(r"^(public|private|protected)\s+(class|static)", s):
        return True
    if re.match(r"^(class|struct|enum)\s+\w", s):
        return True
    if re.match(r"^(template\s*<)", s):
        return True
    if re.match(r"^int\s+main\s*\(", s):
        return True
    if re.match(r"^(void|bool|int|long|char|double|float|auto|unsigned|signed|size_t|string)\s+", s):
        return True
    if re.match(
        r"^(vector|deque|map|set|multimap|multiset|unordered_map|unordered_set|priority_queue|queue|stack|pair|stringstream|bitset)",
        s,
    ):
        return True
    if s in ("{", "}", "} else", "else", "else{"):
        return True
    if s.startswith("for(") or s.startswith("while(") or s.startswith("if(") or s.startswith("switch("):
        return True
    if s.startswith("for ") or s.startswith("while ") or s.startswith("if "):
        return True
    if s.startswith("cout") or s.startswith("cin") or s.startswith("cerr"):
        return True
    if s.startswith("printf") or s.startswith("scanf") or s.startswith("puts"):
        return True
    if s.startswith("return ") and s.endswith(";"):
        return True
    if "::" in s and ("(" in s or s.endswith(";")):
        return True
    if s.endswith(";") and ("(" in s or "[" in s or "=" in s or "::" in s):
        return True
    if re.match(r"^[\w_:<>]+\s+[\w_]+\s*=\s*", s):
        return True
    if re.match(r"^[a-zA-Z_][\w_]*\s*\(", s) and s.endswith(")"):
        return True
    return False


def code_like_ratio(lines: list[str]) -> float:
    nonempty = [ln for ln in lines if ln.strip()]
    if not nonempty:
        return 0.0
    hits = sum(1 for ln in nonempty if is_likely_code_line(ln))
    return hits / len(nonempty)


def fix_nested_links(text: str, in_fence: bool = False) -> str:
    """Flatten nested markdown links like [[[url](url)](url)](url) to [url](url).
    Only applies outside code fences."""
    if in_fence:
        return text

    nested_re = re.compile(r"\[{2,}(https?://[^\]]+)\]\([^)]+\)(?:\]\([^)]+\))+")

    def flatten(m: re.Match[str]) -> str:
        url = m.group(1)
        return f"[{url}]({url})"

    return nested_re.sub(flatten, text)


def fix_nested_links_full(text: str) -> str:
    """Apply nested link fix only outside code fences."""
    fence_re = re.compile(r"(```[\s\S]*?```)", re.MULTILINE)
    parts = fence_re.split(text)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            out.append(fix_nested_links(part))
        else:
            out.append(part)
    return "".join(out)


def linkify_bare_urls(text: str) -> str:
    """Wrap bare http(s) URLs in markdown links; skip URLs inside code fences
    or already inside markdown link syntax."""
    fence_re = re.compile(r"(```[\s\S]*?```)", re.MULTILINE)
    parts = fence_re.split(text)
    url_re = re.compile(r"(?<!\[)(?<!\()https?://[^\s\)\]<>]+")

    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            def sub_url(mm: re.Match[str]) -> str:
                u = mm.group(0).rstrip(".,;:")
                return f"[{u}]({u})"
            out.append(url_re.sub(sub_url, part))
        else:
            out.append(part)
    return "".join(out)


def ensure_title_header(content: str, path: str) -> str:
    """If the file has no markdown header at the top, add one from the filename."""
    lines = content.split("\n")
    for line in lines:
        if line.strip():
            if is_markdown_header_line(line):
                return content
            break

    title = title_from_path(path)
    first_non_empty = ""
    for line in lines:
        if line.strip():
            first_non_empty = line.strip()
            break

    if first_non_empty.startswith("```"):
        return f"# {title}\n\n{content}"
    return f"# {title}\n\n{content}"


def fix_unclosed_fences(content: str) -> str:
    """If there's an odd number of ``` markers, add a closing one at the end."""
    fence_count = len(re.findall(r"^```", content, re.MULTILINE))
    if fence_count % 2 != 0:
        content = content.rstrip() + "\n```\n"
    return content


def format_no_fence(path: str, content: str) -> str:
    """Format files that have no code fences at all."""
    title = title_from_path(path)
    raw = content.replace("\r\n", "\n").rstrip() + "\n"
    lines = raw.split("\n")

    if lines and is_markdown_header_line(lines[0]) and not is_cpp_preprocessor(lines[0]):
        body_lines = lines[1:]
        while body_lines and not body_lines[0].strip():
            body_lines.pop(0)
        bratio = code_like_ratio(body_lines)
        starts_body_cpp = bool(
            body_lines
            and (
                is_cpp_preprocessor(body_lines[0])
                or body_lines[0].strip().startswith("//")
                or body_lines[0].strip().startswith("/*")
                or body_lines[0].strip().startswith("using namespace")
                or body_lines[0].strip().startswith("#include")
            )
        )
        if body_lines and (bratio >= 0.45 or starts_body_cpp):
            head = lines[0].rstrip()
            body = "\n".join(body_lines).rstrip("\n")
            return f"{head}\n\n```cpp\n{body}\n```\n"
        return raw

    ratio = code_like_ratio(lines)
    first = lines[0].strip() if lines else ""
    starts_cpp = bool(
        first
        and (
            is_cpp_preprocessor(lines[0])
            or first.startswith("//")
            or first.startswith("/*")
            or first.startswith("using namespace")
            or first.startswith("#include")
        )
    )

    if ratio >= 0.45 or starts_cpp:
        body = raw.rstrip("\n")
        return f"# {title}\n\n```cpp\n{body}\n```\n"

    if is_markdown_header_line(lines[0]):
        return raw
    return f"# {title}\n\n{raw}"


def process_file(path: str) -> tuple[bool, str]:
    try:
        with open(path, encoding="utf-8", errors="strict") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, encoding="utf-8", errors="replace") as f:
            content = f.read()

    if not content.strip():
        return False, "empty"

    original = content
    new_content = content

    has_fences = "```" in new_content

    if not has_fences:
        new_content = format_no_fence(path, new_content)
    else:
        new_content = fix_unclosed_fences(new_content)

    new_content = ensure_title_header(new_content, path)

    new_content = fix_nested_links_full(new_content)

    new_content = linkify_bare_urls(new_content)

    def norm(s: str) -> str:
        return s.replace("\r\n", "\n")

    if norm(new_content) == norm(original):
        return False, "unchanged"

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    return True, "updated"


def main() -> None:
    root = os.path.abspath(ROOT)
    if not os.path.isdir(root):
        print("Missing", root, file=sys.stderr)
        sys.exit(1)

    updated = 0
    unchanged = 0
    empty = 0
    errors: list[tuple[str, str]] = []

    for dp, _, fs in os.walk(root):
        for name in sorted(fs):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dp, name)
            try:
                changed, status = process_file(path)
            except OSError as e:
                errors.append((path, str(e)))
                continue
            if status == "empty":
                empty += 1
            elif changed:
                updated += 1
                print(f"  UPDATED: {os.path.relpath(path, root)}")
            else:
                unchanged += 1

    total = updated + unchanged + empty
    print(f"\nTotal: {total}, updated: {updated}, empty skipped: {empty}, unchanged: {unchanged}")
    if errors:
        print("Errors:", len(errors))
        for p, msg in errors[:20]:
            print(" ", p, msg)


if __name__ == "__main__":
    main()
