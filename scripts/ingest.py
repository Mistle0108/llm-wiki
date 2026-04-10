#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_INBOX = ROOT / "raw" / "inbox"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "source"


def build_content(title: str, kind: str, added: str, source_url: str) -> str:
    source_line = source_url if source_url else ""
    source_display = source_url if source_url else "n/a"
    return f"""---
title: {title}
kind: {kind}
added: {added}
status: captured
source_url: {source_line}
---

# {title}

Original source URL: {source_display}

## Raw capture

Paste or clip the source content here. Treat this file as immutable after capture.

## Why ingest this

- 

## Notes

- 
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold a new raw source capture in raw/inbox/."
    )
    parser.add_argument("title", help="Human-readable title for the source")
    parser.add_argument("--url", default="", help="Source URL if known")
    parser.add_argument("--kind", default="article", help="Short kind label")
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Capture date in YYYY-MM-DD format",
    )
    args = parser.parse_args()

    slug = slugify(args.title)
    path = RAW_INBOX / f"{args.date}-{slug}.md"

    if path.exists():
        print(f"Refusing to overwrite existing file: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1

    path.write_text(
        build_content(
            title=args.title,
            kind=args.kind,
            added=args.date,
            source_url=args.url,
        ),
        encoding="utf-8",
    )

    print(f"Created {path.relative_to(ROOT)}")
    print("Next steps:")
    print("1. Paste or clip the source content into the new file.")
    print(f"2. Ask Codex to ingest {path.relative_to(ROOT)} into the wiki.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

