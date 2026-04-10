---
title: Home
type: overview
summary: Main landing page for the vault, with the workflow, current seed pages, and what to do next.
created: 2026-04-10
updated: 2026-04-10
---

# Home

This vault starts from the idea in [[wiki/concepts/llm-wiki]]: raw sources stay stable while the maintained wiki gets smarter over time.

## Current seed pages

- [[wiki/sources/karpathy-llm-wiki]]
- [[wiki/sources/obsidian-web-clipper]]
- [[wiki/concepts/ingest-query-lint]]
- [[wiki/entities/obsidian-web-clipper]]
- [[wiki/synthesis/current-thesis]]

## Working loop

1. Capture a source in `raw/inbox/`.
2. Ask Codex to ingest it.
3. Review the changed wiki pages in Obsidian.
4. Ask follow-up questions and file reusable answers back into the vault.
5. Run `python3 scripts/lint.py` every so often to catch drift.

## Next actions

- Add the first real source that matters to your own learning or project.
- Let Codex update several pages from that one source instead of keeping notes in chat.
- Use [[index]] and Obsidian graph view to watch structure emerge.
- If the source is on the web, use [[wiki/entities/obsidian-web-clipper]] as the default intake path.
