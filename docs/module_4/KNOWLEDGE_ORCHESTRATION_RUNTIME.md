# Telecom AI Knowledge Orchestration Runtime

## Purpose

This document describes the deployment-oriented runtime implemented in:

```text
notebooks/module_4/21_module4_knowledge_orchestration_runtime.ipynb
```

Notebook 21 is the deployment culmination of Module 4. It does not replace the frozen formal research notebook:

```text
notebooks/module_4/20_rag_mcp_hybrid.ipynb
```

## Public Runtime Name

**Telecom AI Knowledge Orchestration Runtime**

## Canonical Runtime

**Cell 4D / internal 6Y v1.3**

The internal `MODULE 4C.6Y` and `4C6*` identifiers are retained to preserve validated compatibility.

## Runtime Architecture

```text
User
 ↓
Deterministic Security
 ↓
Granite Knowledge-Scope Router
 ├─ Connected Technical Corpus
 │    ↓
 │  Gemma Retrieval Planner
 │    ├─ RAG_ONLY
 │    ├─ MCP_ONLY
 │    └─ HYBRID
 │    ↓
 │  Adaptive Evidence Loop
 │    ↓
 │  Grounded Gemma
 │    ↓
 │  Frozen Granite Comparative Judge
 │
 ├─ Live External Scope
 │    ├─ date/time → local runtime
 │    └─ changing public facts → Open-WebSearch CLI
 │
 └─ Stable General Knowledge
      ↓
    Gemma fallback + scope caveat
```

## Deployment Adaptation

The formal Module 4 experiment used the persistent Version B Knowledge MCP architecture.

Notebook 21 intentionally uses **MCP Version A remote query-time retrieval** to avoid carrying the approximately 69 GB Version B persistent deployment footprint while preserving telecom knowledge access.

This is a deployment decision, not a retrospective modification of the frozen experiment.

## Connected Knowledge Path

The planner selects the minimum sufficient retrieval architecture:

- `RAG_ONLY`
- `MCP_ONLY`
- `HYBRID`

Search policy:

- one search required,
- second search when evidence requirements remain unresolved,
- third search only when still required,
- hard maximum of three searches.

## Live External Path

Changing public facts use:

```text
open-websearch@2.1.11
```

through its CLI JSON interface.

The final notebook does not use Open-WebSearch as an MCP transport because STDIO MCP execution under Jupyter exposed an `ipykernel` / `fileno` incompatibility.

## Local Runtime Path

Direct date/time questions use Python `datetime` + `zoneinfo`.

This avoids asking a web search engine to establish the runtime's current clock.

## General Knowledge Path

Stable questions outside the connected corpus and not requiring live external information use Gemma general knowledge with a visible scope caveat.

## Evaluation Boundary

The frozen Granite comparative judge applies only when connected-corpus evidence is available.

The reported hallucination-risk estimate is evidence-relative; it is not a universal factuality score.

## 6Z Decision

A post-generation knowledge-gap escalation layer was evaluated but not adopted.

Semantically clear current/person questions already route directly to `LIVE_EXTERNAL_GROUNDED`, so the extra escalation layer added complexity without sufficient architectural benefit.
