---
title: Ingest Query Lint
type: concept
summary: The three core loops for maintaining a wiki: add new knowledge, answer questions from the maintained pages, and periodically health-check the structure.
created: 2026-04-10
updated: 2026-04-10
---

# Ingest Query Lint

The wiki stays healthy because it is maintained through three repeated operations.

## Ingest

Read a raw source, summarize it, update the source page, update any affected concept or entity pages, then refresh [[index]] and append to [[log]].

For web sources, [[wiki/entities/obsidian-web-clipper]] is a practical capture path into `raw/inbox/`.

## Query

Read [[index]] first, then the most relevant wiki pages. Answer from the maintained wiki, not from vague memory. If the answer is durable, file it back into the vault.

## Lint

Check for structural and semantic drift: broken links, orphan pages, stale claims, duplicate concepts, missing cross-references, and places where a new source should update an existing page.

## Related pages

- [[wiki/concepts/llm-wiki]]
- [[wiki/sources/karpathy-llm-wiki]]
