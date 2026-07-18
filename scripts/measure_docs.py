#!/usr/bin/env python3
"""Produce reproducible reading-load and duplication measurements."""

from __future__ import annotations

import math
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    ROOT / "chapters/01-computing-foundations.md",
    ROOT / "chapters/02-programming-foundations.md",
    ROOT / "chapters/03-software-engineering.md",
    ROOT / "chapters/04-internet-web-and-apis.md",
]
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*")
LINK_RE = re.compile(r"\[([^]]+)]\([^)]+\)")
ENTRY_SPLIT_RE = re.compile(r"^## ", re.MULTILINE)
NAVIGATION_SPLIT_RE = re.compile(
    r"^### (?:Related concepts in TFB|Deeper concepts|Further reading)\s*$",
    re.MULTILINE,
)


def visible_text(markdown: str) -> str:
    """Remove link destinations and Markdown punctuation while retaining visible text."""
    text = LINK_RE.sub(r"\1", markdown)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    return text


def word_count(markdown: str) -> int:
    return len(WORD_RE.findall(visible_text(markdown)))


def entries(markdown: str) -> list[tuple[str, str]]:
    result = []
    for section in ENTRY_SPLIT_RE.split(markdown)[1:]:
        title, _, body = section.partition("\n")
        if title in {"Chapter map", "Chapter status"}:
            continue
        result.append((title, body))
    return result


def repeated_long_paragraphs() -> int:
    occurrences: dict[str, set[Path]] = defaultdict(set)
    paths = sorted((ROOT / "chapters").glob("*.md"))
    paths += sorted((ROOT / "further").glob("*.md"))
    for path in paths:
        for paragraph in re.split(r"\n\s*\n", path.read_text()):
            if paragraph.lstrip().startswith(("#", "-", "```")):
                continue
            plain = " ".join(visible_text(paragraph).lower().split())
            if len(WORD_RE.findall(plain)) >= 40:
                occurrences[plain].add(path)
    return sum(1 for paths in occurrences.values() if len(paths) > 1)


def main() -> None:
    print("Word counting: visible Markdown text; link destinations excluded.")
    print("Reading time: complete page words / 200 words per minute, rounded up.")
    for path in CHAPTERS:
        markdown = path.read_text()
        chapter_entries = entries(markdown)
        prose_counts = []
        for _, body in chapter_entries:
            prose = NAVIGATION_SPLIT_RE.split(body, maxsplit=1)[0]
            prose_counts.append(word_count(prose))
        total = word_count(markdown)
        print(
            f"{path.relative_to(ROOT)}: entries={len(chapter_entries)} "
            f"words={total} minutes={math.ceil(total / 200)} "
            f"entry_prose_min={min(prose_counts)} "
            f"entry_prose_max={max(prose_counts)}"
        )
    print(f"Repeated long prose paragraphs: {repeated_long_paragraphs()}")


if __name__ == "__main__":
    main()
