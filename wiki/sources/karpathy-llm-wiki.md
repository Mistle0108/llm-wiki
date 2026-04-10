---
title: Karpathy LLM Wiki Gist
type: source
summary: Source page for the gist that proposes a three-layer system of raw sources, maintained wiki pages, and an agent schema.
created: 2026-04-10
updated: 2026-04-10
source_path: raw/inbox/2026-04-10-karpathy-llm-wiki.md
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

# Karpathy LLM Wiki Gist

## Summary

The source argues that LLMs should maintain a persistent wiki rather than repeatedly reconstructing knowledge from raw files at question time.

## Key takeaways

- The useful unit is a maintained markdown page, not a transient retrieval result.
- A wiki should be operated through repeated ingest, query, and lint loops.
- `index.md` and `log.md` act as lightweight coordination primitives before heavier search infrastructure is needed.
- Obsidian works well as the visual IDE for browsing links, graph structure, and page evolution.

## Implementation notes for this repo

- The source became the first raw capture at [[raw/inbox/2026-04-10-karpathy-llm-wiki]].
- The schema for future sessions lives in [[AGENTS]].
- The starter synthesis based on this source is in [[wiki/synthesis/current-thesis]].

