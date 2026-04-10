---
title: LLM Wiki
type: concept
summary: A persistent wiki maintained by an LLM so knowledge is compiled once, updated over time, and reused across future questions.
created: 2026-04-10
updated: 2026-04-10
---

# LLM Wiki

An LLM wiki is a maintained layer of structured markdown that sits between raw source material and future questions.

## Core idea

Traditional RAG systems retrieve fragments from raw documents for each question. The `LLM Wiki` pattern instead compiles knowledge into durable pages that are revised as new material arrives.

## Why it matters

- Cross-references accumulate instead of being rediscovered each time.
- Contradictions can be surfaced and tracked in the wiki itself.
- High-value syntheses become durable artifacts instead of disappearing into chat history.

## Main layers

- `raw/` contains source-of-truth captures.
- `wiki/` contains maintained summaries, entities, concepts, and syntheses.
- [[AGENTS]] describes how the agent should behave.

## Related pages

- [[wiki/concepts/ingest-query-lint]]
- [[wiki/sources/karpathy-llm-wiki]]
- [[wiki/synthesis/current-thesis]]

