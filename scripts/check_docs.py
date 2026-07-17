#!/usr/bin/env python3
"""Run lightweight, dependency-free checks over TFB Markdown files."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_PARTS = {".git"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
HTML_RE = re.compile(r"<[^>]+>")
PUNCTUATION_RE = re.compile(r"[^\w\- ]", re.UNICODE)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in EXCLUDED_PARTS for part in path.parts)
    )


def github_slug(text: str) -> str:
    text = re.sub(r"\s+#+\s*$", "", text.strip())
    text = HTML_RE.sub("", text).lower()
    text = PUNCTUATION_RE.sub("", text)
    return re.sub(r"[ ]+", "-", text)


def headings(path: Path) -> tuple[set[str], list[str]]:
    anchors: set[str] = set()
    anchor_counts: defaultdict[str, int] = defaultdict(int)
    sibling_counts: defaultdict[tuple[tuple[str, ...], str], int] = defaultdict(int)
    stack: list[str] = []
    errors: list[str] = []
    in_fence = False

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        match = HEADING_RE.match(line)
        if not match:
            continue

        level = len(match.group(1))
        title = match.group(2)
        slug = github_slug(title)
        base_count = anchor_counts[slug]
        anchor_counts[slug] += 1
        anchors.add(slug if base_count == 0 else f"{slug}-{base_count}")

        stack = stack[: level - 1]
        parent = tuple(stack)
        sibling_key = (parent, slug)
        sibling_counts[sibling_key] += 1
        if sibling_counts[sibling_key] > 1:
            relative = path.relative_to(ROOT)
            errors.append(
                f"{relative}:{line_number}: duplicate sibling heading '{title}'"
            )

        while len(stack) < level - 1:
            stack.append("")
        stack.append(slug)

    return anchors, errors


def check_links(path: Path, anchor_index: dict[Path, set[str]]) -> list[str]:
    errors: list[str] = []
    in_fence = False

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for match in LINK_RE.finditer(line):
            target = unquote(match.group(1).strip("<>"))
            if target.startswith(("http://", "https://", "mailto:")):
                continue

            target_path_text, separator, fragment = target.partition("#")
            target_path = (
                path if not target_path_text else (path.parent / target_path_text).resolve()
            )
            relative = path.relative_to(ROOT)

            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{relative}:{line_number}: link escapes the repository: {target}"
                )
                continue

            if not target_path.exists():
                errors.append(f"{relative}:{line_number}: missing link target: {target}")
                continue

            if separator and fragment and target_path.suffix.lower() == ".md":
                expected = github_slug(fragment)
                if expected not in anchor_index.get(target_path, set()):
                    errors.append(
                        f"{relative}:{line_number}: missing heading anchor: {target}"
                    )

    return errors


def check_outline() -> list[str]:
    path = ROOT / "OUTLINE.md"
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    chapter_matches = list(re.finditer(r"^## (\d+)\. ", text, re.MULTILINE))
    numbers = [int(match.group(1)) for match in chapter_matches]
    if numbers != list(range(1, 14)):
        errors.append("OUTLINE.md: expected chapter sections numbered 1 through 13")

    total_first_pass_entries = 0

    for index, match in enumerate(chapter_matches):
        end = chapter_matches[index + 1].start() if index + 1 < len(chapter_matches) else len(text)
        section = text[match.start() : end]
        required = ("### First pass", "### Further territory", "### Recognition and landscape")
        for heading in required:
            if heading not in section:
                errors.append(
                    f"OUTLINE.md: Chapter {match.group(1)} is missing '{heading}'"
                )

        first_pass = section.partition("### First pass")[2].partition("### Further territory")[0]
        entry_count = len(re.findall(r"^\d+\. ", first_pass, re.MULTILINE))
        total_first_pass_entries += entry_count
        if not 5 <= entry_count <= 8:
            errors.append(
                f"OUTLINE.md: Chapter {match.group(1)} has {entry_count} first-pass entries; expected 5-8"
            )

        landscape = section.partition("### Recognition and landscape")[2]
        if not re.search(
            r"^\*Landscape selection reviewed: \d{4}-\d{2}-\d{2}; verify current status before publication\.\*$",
            landscape,
            re.MULTILINE,
        ):
            errors.append(
                f"OUTLINE.md: Chapter {match.group(1)} is missing the current landscape review marker"
            )

    if total_first_pass_entries > 95:
        errors.append(
            f"OUTLINE.md: {total_first_pass_entries} first-pass entries exceed the 95-entry breadth guardrail"
        )

    return errors


def main() -> int:
    files = markdown_files()
    anchor_index: dict[Path, set[str]] = {}
    errors: list[str] = []

    for path in files:
        anchor_index[path], heading_errors = headings(path)
        errors.extend(heading_errors)

    for path in files:
        errors.extend(check_links(path, anchor_index))

    errors.extend(check_outline())

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation checks passed. Checked {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
