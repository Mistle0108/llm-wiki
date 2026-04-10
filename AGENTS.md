# LLM Wiki Agent Guide

This file is the operating schema for Codex in this repository. Treat it as the source of truth for how the wiki should be maintained.

## Mission

Maintain a persistent, compounding wiki that sits between the user and the raw sources.

- `raw/` is human-curated source material and should be treated as immutable after capture.
- `wiki/` is LLM-maintained knowledge and should evolve over time.
- `index.md` is the main content map.
- `log.md` is the append-only operational history.

## Directory rules

- Put untouched source captures in `raw/inbox/`.
- Put downloaded media in `raw/assets/`.
- Put high-level orientation pages in `wiki/overviews/`.
- Put topic and framework pages in `wiki/concepts/`.
- Put named-thing pages in `wiki/entities/`.
- Put one wiki summary page per source in `wiki/sources/`.
- Put durable answers to specific questions in `wiki/queries/`.
- Put cross-source rollups and evolving theses in `wiki/synthesis/`.

## Page conventions

All pages in `wiki/` should begin with YAML frontmatter using this minimum shape:

```yaml
---
title: ...
type: overview | concept | entity | source | query | synthesis
summary: ...
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Additional source-page fields:

```yaml
source_path: raw/inbox/...
source_url: https://...
```

Formatting conventions:

- Use lowercase kebab-case filenames.
- Prefer Obsidian wikilinks for internal links.
- When linking outside the current folder, use repo-relative wikilinks such as `[[wiki/concepts/llm-wiki]]`.
- Keep summaries crisp and factual.
- Preserve uncertainty explicitly instead of smoothing it over.
- When newer material changes an older claim, update the affected page and note the change.

## Ingest workflow

When the user asks to ingest a source:

1. Read the raw source in `raw/inbox/`.
2. Discuss key takeaways with the user if needed.
3. Create or update the matching page in `wiki/sources/`.
4. Update any affected concept, entity, overview, or synthesis pages.
5. Update `index.md` if any page was added or its summary changed materially.
6. Append a new entry to `log.md` with the prefix `## [YYYY-MM-DD] ingest | ...`.

During ingest:

- Never delete or rewrite the raw source as part of synthesis.
- Prefer updating existing wiki pages over creating near-duplicates.
- Add links in both directions when a new page meaningfully connects to an existing page.
- If a source is low-value, record that fact briefly instead of inventing importance.

## Query workflow

When the user asks a question about the wiki:

1. Read `index.md` first.
2. Open the most relevant pages in `wiki/`.
3. Synthesize an answer grounded in the maintained pages and raw sources.
4. Cite the pages or source pages used.
5. If the answer is likely to be useful again, offer to file it under `wiki/queries/` or `wiki/synthesis/`.

## Lint workflow

When the user asks for a health check:

1. Run `python3 scripts/lint.py`.
2. Inspect the reported structural issues.
3. Perform a semantic pass for contradictions, stale claims, weak summaries, missing links, and missing pages.
4. Append a `lint` entry to `log.md` if changes or findings were substantial.

## Editing posture

- Raw files are immutable after capture unless the user explicitly wants to fix a capture mistake.
- The wiki is allowed to be rewritten aggressively when structure improves.
- Favor a small number of rich pages over many shallow pages.
- Do not let `index.md` drift out of date.
- Keep `log.md` append-only.

