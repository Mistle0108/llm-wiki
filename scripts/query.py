#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEARCH_PATHS = [ROOT / "index.md", ROOT / "wiki"]


@dataclass
class PageMatch:
    path: Path
    title: str
    summary: str
    score: int


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for search_path in SEARCH_PATHS:
        if search_path.is_file():
            files.append(search_path)
        elif search_path.is_dir():
            files.extend(sorted(search_path.rglob("*.md")))
    return files


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    raw_frontmatter, body = parts
    frontmatter: dict[str, str] = {}
    for line in raw_frontmatter.splitlines()[1:]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter, body


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def fallback_summary(body: str) -> str:
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        return re.sub(r"\s+", " ", line)
    return ""


def score_text(query: str, title: str, summary: str, body: str) -> int:
    query_lower = query.lower()
    tokens = [token for token in re.split(r"\s+", query_lower) if token]

    score = 0
    title_lower = title.lower()
    summary_lower = summary.lower()
    body_lower = body.lower()

    if query_lower in title_lower:
        score += 20
    if query_lower in summary_lower:
        score += 10
    if query_lower in body_lower:
        score += 5

    for token in tokens:
        score += title_lower.count(token) * 5
        score += summary_lower.count(token) * 3
        score += body_lower.count(token)

    return score


def main() -> int:
    parser = argparse.ArgumentParser(description="Search index.md and wiki/*.md.")
    parser.add_argument("query", help="Search string")
    parser.add_argument("--limit", type=int, default=8, help="Maximum matches to print")
    args = parser.parse_args()

    matches: list[PageMatch] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)
        title = frontmatter.get("title") or first_heading(body) or path.stem
        summary = frontmatter.get("summary") or fallback_summary(body)
        score = score_text(args.query, title, summary, body)
        if score <= 0:
            continue
        matches.append(PageMatch(path=path, title=title, summary=summary, score=score))

    matches.sort(key=lambda item: (-item.score, item.path.as_posix()))

    if not matches:
        print(f'No matches for "{args.query}".', file=sys.stderr)
        return 1

    print(f'Top matches for "{args.query}":')
    for match in matches[: args.limit]:
        rel_path = match.path.relative_to(ROOT).as_posix()
        print(f"- [{match.score:>3}] {rel_path}")
        if match.summary:
            print(f"      {match.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

