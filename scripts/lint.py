#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
INDEX_PATH = ROOT / "index.md"
LOG_PATH = ROOT / "log.md"
REQUIRED_FIELDS = {"title", "type", "summary", "created", "updated"}
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
LOG_HEADING_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] [a-z-]+ \| .+")


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


def all_markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def wiki_pages() -> list[Path]:
    return sorted(WIKI_DIR.rglob("*.md"))


def aliases_for(paths: list[Path]) -> tuple[dict[str, str], dict[str, Path]]:
    stem_counts = Counter(path.stem for path in paths)
    alias_map: dict[str, str] = {}
    canonical_to_path: dict[str, Path] = {}

    for path in paths:
        rel = path.relative_to(ROOT).with_suffix("").as_posix()
        canonical_to_path[rel] = path
        alias_map[rel] = rel
        if stem_counts[path.stem] == 1:
            alias_map[path.stem] = rel
    return alias_map, canonical_to_path


def extract_wikilinks(text: str) -> list[str]:
    links: list[str] = []
    for raw_target in WIKILINK_RE.findall(text):
        target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.append(target)
    return links


def lint_frontmatter(pages: list[Path]) -> list[str]:
    issues: list[str] = []
    for path in pages:
        frontmatter, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        missing = sorted(field for field in REQUIRED_FIELDS if field not in frontmatter)
        if missing:
            issues.append(
                f"{path.relative_to(ROOT).as_posix()}: missing frontmatter fields {', '.join(missing)}"
            )
        if frontmatter.get("type") == "source" and "source_path" not in frontmatter:
            issues.append(f"{path.relative_to(ROOT).as_posix()}: source page missing source_path")
        source_path = frontmatter.get("source_path")
        if source_path and not (ROOT / source_path).exists():
            issues.append(
                f"{path.relative_to(ROOT).as_posix()}: source_path does not exist -> {source_path}"
            )
    return issues


def lint_links(all_paths: list[Path], wiki_paths: list[Path]) -> tuple[list[str], list[str]]:
    alias_map, canonical_to_path = aliases_for(all_paths)
    broken: list[str] = []
    inbound_counts: defaultdict[str, int] = defaultdict(int)

    for path in all_paths:
        text = path.read_text(encoding="utf-8")
        for link in extract_wikilinks(text):
            canonical = alias_map.get(link)
            if canonical is None:
                broken.append(f"{path.relative_to(ROOT).as_posix()}: unresolved wikilink [[{link}]]")
                continue
            inbound_counts[canonical] += 1

    orphans: list[str] = []
    for page in wiki_paths:
        canonical = page.relative_to(ROOT).with_suffix("").as_posix()
        if inbound_counts.get(canonical, 0) == 0:
            orphans.append(f"{page.relative_to(ROOT).as_posix()}: no inbound links")

    return broken, orphans


def lint_index(wiki_paths: list[Path]) -> list[str]:
    issues: list[str] = []
    if not INDEX_PATH.exists():
        return ["index.md is missing"]

    alias_map, _ = aliases_for(all_markdown_files())
    index_links = {
        alias_map[link]
        for link in extract_wikilinks(INDEX_PATH.read_text(encoding="utf-8"))
        if link in alias_map
    }

    for path in wiki_paths:
        canonical = path.relative_to(ROOT).with_suffix("").as_posix()
        if canonical not in index_links:
            issues.append(f"{path.relative_to(ROOT).as_posix()}: not referenced from index.md")
    return issues


def lint_log() -> list[str]:
    if not LOG_PATH.exists():
        return ["log.md is missing"]

    issues: list[str] = []
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("## [") and not LOG_HEADING_RE.match(line):
            issues.append(f"log.md: malformed heading -> {line}")
    return issues


def main() -> int:
    all_paths = all_markdown_files()
    wiki_paths = wiki_pages()

    issues: list[str] = []
    issues.extend(lint_frontmatter(wiki_paths))

    broken_links, orphan_pages = lint_links(all_paths, wiki_paths)
    issues.extend(broken_links)
    issues.extend(orphan_pages)
    issues.extend(lint_index(wiki_paths))
    issues.extend(lint_log())

    if issues:
        print("Lint issues found:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Lint passed: no structural issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
