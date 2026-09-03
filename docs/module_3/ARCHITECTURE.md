# Module 3 Architecture Notes

## Design objective

Expose telecom knowledge through one provider-neutral MCP interface while comparing two retrieval implementations under frozen experiment controls.

## Version A — direct remote retrieval

```text
LLM → FastMCP → deterministic route selection → remote 3GPP/TCC retrieval → bounded evidence → LLM
```

**Strengths:** lightweight, no persistent local index build, useful for rapid experimentation.

**Trade-offs:** query-time remote I/O, dependency on external source availability and variable network latency.

## Version B — persistent BM25/FTS retrieval

```text
Build: corpus planning → normalization → hash deduplication → telecom tokenization → 21 DuckDB BM25/FTS shards → persistence
Runtime: LLM → FastMCP → deterministic route selection → persistent shards → bounded evidence → LLM
```

**Strengths:** corpus snapshot control, repeatable retrieval, reduced dependence on query-time remote availability and clear build/runtime separation.

**Trade-offs:** artifact lifecycle/storage, rebuilds when the corpus changes, and the fact that structurally stronger retrieval does not automatically guarantee better downstream grounding.

## Central system finding

The MCP abstraction standardized the **tool contract**, but did not standardize model behaviour. Query formulation, search iteration, evidence consumption, latency and final-answer grounding remained model/provider dependent.

## Production implication

Retain a common MCP interface, but apply model-specific runtime profiles for search budget, output budget, evidence volume, reasoning behaviour and latency controls.
