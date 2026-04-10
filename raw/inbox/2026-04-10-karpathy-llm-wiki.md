---
title: LLM Wiki
kind: gist
added: 2026-04-10
status: captured
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

# LLM Wiki

Original source URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Capture note

This is the seed source for the repository setup. The canonical source remains the remote gist.

## Key points captured from the source

- Build a persistent wiki between the user and raw documents instead of rediscovering knowledge through ad hoc retrieval each time.
- Treat the system as three layers: raw sources, the maintained wiki, and an agent schema that describes the workflow.
- Operate the wiki through three recurring loops: ingest, query, and lint.
- Keep a content-oriented `index.md` and a chronological `log.md`.
- Use small local tools only when the wiki grows enough that simple file navigation stops being sufficient.

## Notes

- This file should remain stable after capture.
- Future synthesis belongs in `wiki/`, not here.

