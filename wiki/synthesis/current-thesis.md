---
title: Current Thesis
type: synthesis
summary: Initial thesis for this repository: start with lightweight markdown workflows, let Codex maintain structure, and add heavier tooling only when the wiki earns it.
created: 2026-04-10
updated: 2026-04-10
---

# Current Thesis

This repository should begin as a plain Git repo of markdown files that happens to open cleanly in Obsidian.

## Starting assumptions

- The wiki is small enough that [[index]] plus simple search is enough.
- Codex should do the repetitive bookkeeping work of keeping pages aligned.
- New tooling should be added only when the existing workflow becomes painful.

## Practical implications

- Focus on capturing good sources and maintaining a few strong pages first.
- Prefer updating an existing page over creating a redundant new one.
- Keep raw captures stable and put interpretation in the wiki layer.
- Use practical local-first intake tools such as [[wiki/entities/obsidian-web-clipper]] when they reduce capture friction.
- Use `python3 scripts/lint.py` to keep the structure honest.

## Revisit later

- Add richer entity coverage once repeated names start appearing across sources.
- Add `qmd` or another dedicated search tool when `index.md` and `rg` stop being enough.
- Add Dataview or Marp only if the wiki actually starts to need those output formats.

## Related pages

- [[wiki/concepts/llm-wiki]]
- [[wiki/concepts/ingest-query-lint]]
- [[wiki/sources/karpathy-llm-wiki]]
- [[wiki/sources/obsidian-web-clipper]]
