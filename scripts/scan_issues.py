#!/usr/bin/env python3
"""Scan all md files for formatting issues."""
import os
import re

root = os.path.join(os.path.dirname(__file__), "..", "src", "questions")
root = os.path.normpath(root)

unclosed = []
no_lang = []
no_header = []
nested_links = []

for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        try:
            t = open(p, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        if not t.strip():
            continue

        fence_pattern = re.compile(r"^```", re.MULTILINE)
        fences = fence_pattern.findall(t)
        if len(fences) % 2 != 0:
            unclosed.append(p)

        lines = t.split("\n")
        in_fence = False
        for line in lines:
            stripped = line.strip()
            if re.match(r"^```", stripped):
                if not in_fence:
                    if stripped == "```":
                        no_lang.append(p)
                        break
                    in_fence = True
                else:
                    in_fence = False

        first_non_empty = ""
        for line in lines:
            if line.strip():
                first_non_empty = line.strip()
                break
        if not re.match(r"^#{1,6}\s", first_non_empty):
            no_header.append((p, first_non_empty[:80]))

        if re.search(r"\[\[", t):
            nested_links.append(p)

print("=== UNCLOSED FENCES ===")
for p in sorted(unclosed):
    print(f"  {p}")
print(f"Total: {len(unclosed)}")

print("\n=== NO LANGUAGE TAG ON OPENING FENCE ===")
for p in sorted(no_lang):
    print(f"  {p}")
print(f"Total: {len(no_lang)}")

print("\n=== MISSING TITLE HEADER ===")
for p, ctx in sorted(no_header):
    print(f"  {p}  -> starts with: {ctx}")
print(f"Total: {len(no_header)}")

print("\n=== POSSIBLE NESTED LINKS ===")
for p in sorted(nested_links):
    print(f"  {p}")
print(f"Total: {len(nested_links)}")
