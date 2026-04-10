# MyLLMWiki

This repository is an Obsidian-friendly LLM wiki. Raw source material lives in `raw/`, the maintained knowledge base lives in `wiki/`, and [`AGENTS.md`](./AGENTS.md) tells Codex how to ingest, query, and lint the vault.

## Layout

- `raw/inbox/`: immutable source captures waiting to be ingested
- `raw/assets/`: downloaded attachments and images
- `wiki/overviews/`: landing pages and top-level maps
- `wiki/concepts/`: topic summaries and frameworks
- `wiki/entities/`: people, orgs, tools, places, or other named things
- `wiki/sources/`: one page per raw source after ingest
- `wiki/queries/`: reusable answers that were worth filing back into the vault
- `wiki/synthesis/`: higher-level theses, comparisons, and rollups
- `index.md`: content map of the wiki
- `log.md`: append-only timeline of setup, ingests, queries, and lint passes

## Basic workflow

1. Capture a source in `raw/inbox/`.
2. Ask Codex to ingest that source into the wiki.
3. Review the updated pages in Obsidian.
4. Ask questions against the wiki.
5. File good answers back into `wiki/queries/` or `wiki/synthesis/`.
6. Run `python3 scripts/lint.py` occasionally to catch structural issues.

## Helpful commands

```bash
python3 scripts/ingest.py "Article title" --url "https://example.com"
python3 scripts/query.py "persistent wiki"
python3 scripts/lint.py
./scripts/open-vault.sh
```

`ingest.py` scaffolds a raw source file. The actual synthesis still happens through Codex following the rules in [`AGENTS.md`](./AGENTS.md).

## Obsidian setup

- Open this folder as a vault.
- In Obsidian, set the attachment folder path to `raw/assets/` if you want downloaded images kept locally.
- This repo already includes a starter `.obsidian/` config and `templates/` folder.
- Use the Templates core plugin with `templates/raw-source.md`, `templates/query-note.md`, and `templates/synthesis-note.md`.
- Optional plugins later: Dataview, Marp, and Web Clipper.

## Starting point

The vault is seeded with the Karpathy `LLM Wiki` gist that inspired this setup:

- raw capture: [`raw/inbox/2026-04-10-karpathy-llm-wiki.md`](./raw/inbox/2026-04-10-karpathy-llm-wiki.md)
- source page: [`wiki/sources/karpathy-llm-wiki.md`](./wiki/sources/karpathy-llm-wiki.md)
- concept page: [`wiki/concepts/llm-wiki.md`](./wiki/concepts/llm-wiki.md)
