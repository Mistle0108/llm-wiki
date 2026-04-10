---
title: Next Steps
type: overview
summary: Short operational checklist for what to do next in this vault after the initial bootstrap.
created: 2026-04-10
updated: 2026-04-10
---

# Next Steps

## Immediate

1. Open this repository as an Obsidian vault.
2. Review [[wiki/overviews/home]] and [[index]].
3. Add one real source to `raw/inbox/`.
4. Ask Codex to ingest that source into the wiki.

## First good source ideas

- An article or paper you already know is important.
- Notes from a project you are actively working on.
- A transcript, memo, or long-form write-up you expect to revisit.

## After the first ingest

- Inspect which pages changed in `wiki/`.
- Tighten summaries and links where the structure feels weak.
- Ask one cross-source question and file the answer back into `wiki/queries/` if it seems reusable.
- Run `python3 scripts/lint.py`.

## Later

- Add Dataview if frontmatter-driven tables become useful.
- Add Marp only if you start exporting decks.
- Add `qmd` only when `index.md` plus basic search stops being enough.

