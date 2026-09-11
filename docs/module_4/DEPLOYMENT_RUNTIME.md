# Module 4 Deployment Runtime

## Objective

Translate the validated Module 4 knowledge-access research into a practical deployment runtime without modifying the frozen formal experiment.

## Operational Path

A production-facing interface should prioritize:

```text
Question
 ↓
Security
 ↓
Knowledge-Scope Router
 ↓
Selected Knowledge Path
 ↓
Answer
```

The baseline Gemma comparison and Granite comparative judge are research/evaluation features and should not be mandatory blockers on every production response.

## Hosted Models

- Generator: `google/gemma-4-26b-a4b-it`
- Knowledge router / comparative judge: `ibm-granite/granite-4.2-8b`

## Local Runtime Components

- BGE-M3 embedding model
- FAISS RAG index
- metadata shards
- Python security/runtime utilities

## Remote Knowledge Components

- MCP Version A 3GPP access
- GSMA Telecom Common Corpus access
- Open-WebSearch CLI for live external information

## Future UI

A Streamlit deployment can expose:

- question input,
- selected knowledge scope,
- selected retrieval architecture,
- answer,
- evidence cards,
- `[E#]` citations,
- search/retrieval diagnostics,
- optional latency/evaluation panel.

## Repository Placement

Notebook 21 remains under:

```text
notebooks/module_4/
```

Deployment-specific documentation remains under:

```text
docs/module_4/
```

A separate repository is not required at this stage.
