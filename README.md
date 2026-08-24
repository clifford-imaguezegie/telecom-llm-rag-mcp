# Telecom LLM, RAG & MCP

An experimental project exploring the application of **telecom-domain Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), and AI-driven autonomous network operations**.

## Project Objective

The objective of this project is to investigate how a telecom-domain LLM can be progressively combined with enterprise knowledge retrieval and operational tools to support increasingly intelligent and autonomous network operations.

The project follows a progressive architecture:

1. **LLM Baseline** — Establish and evaluate a telecom-domain LLM against a general-purpose LLM.
2. **RAG** — Ground the model with relevant and continuously updated telecom knowledge.
3. **Evaluation** — Measure performance across conceptual, standards-based and applied engineering scenarios.
4. **MCP** — Provide controlled access to simulated network data, diagnostics and operational tools.
5. **AI Network Operations** — Explore AI-assisted fault diagnosis, remediation and verification.
6. **Autonomous Operations** — Investigate closed-loop AI-driven telecom network operations.

## Project Roadmap

| Module | Description | Status |
|---|---|---|
| **001_llm_base** | LLM baseline and comparative telecom benchmark | ✅ **Completed** |
| **002_rag** | Retrieval-Augmented Generation for telecom knowledge grounding | ⏳ Planned |
| **003_mcp** | Model Context Protocol integration with network tools | ⏳ Planned |
| **004_agents** | AI agents for telecom reasoning and operational workflows | ⏳ Planned |
| **005_autonomous_telecom** | Autonomous telecom operations and closed-loop automation | ⏳ Planned |

## Module 1 — LLM Baseline

The completed baseline establishes a controlled comparison between:

- **General LLM:** `EssentialAI/rnj-1-instruct`
- **Telecom LLM:** `farbodtavakkoli/OTel-LLM-8.3B-IT`

The evaluation uses two complementary benchmark tracks:

### Track 1 — Custom Telecom Benchmark

A **20-question custom telecom benchmark** covering:

- 5G Core
- 5G RAN
- 5G SA procedures
- Open RAN
- Cloud-native telecom
- Applied telecom engineering
- Capacity planning
- Troubleshooting
- Network architecture

### Track 2 — Industry Benchmark

A **32-question industry benchmark** based on selected GSMA Open-Telco Lite benchmark material covering:

- 3GPP working-group classification
- O-RAN
- 6G decision reasoning
- srsRAN
- Telecom mathematics
- Telecom standards Q&A
- TELETABLES
- Drive-test analysis

### Evaluation Approach

The final benchmark assessment is based on **independent expert technical review** against benchmark reference answers and expected technical criteria.

Track 1 also included an Independent LLM Judge as a supplementary evaluation layer. Track 2 was evaluated directly against the benchmark references and expert review.

### Module 1 Outcome

The expert review identified the **General LLM as the stronger overall baseline**, with broader coverage and stronger performance on applied engineering, troubleshooting, cloud-native architecture and complex telecom reasoning.

OTel 1.0 demonstrated strengths on selected focused telecom and standards-based questions but showed greater difficulty with complex open-ended tasks and a higher rate of non-responsive answers.

A key baseline finding is:

> **Technical fluency does not guarantee technical correctness.**

The baseline results will be used as the reference point for evaluating the incremental value of RAG, MCP and subsequent autonomous-operation capabilities.

## Architecture

The project will progressively evolve towards:

```text
                    ┌─────────────────────┐
                    │    Telecom LLM      │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                                 │
       ┌──────▼──────┐                   ┌──────▼──────┐
       │     RAG     │                   │     MCP     │
       └──────┬──────┘                   └──────┬──────┘
              │                                 │
       Telecom Knowledge                 Network Tools
              │                                 │
              └────────────────┬────────────────┘
                               │
                     ┌─────────▼─────────┐
                     │ Simulated Network │
                     └─────────┬─────────┘
                               │
                     ┌─────────▼─────────┐
                     │ AI Network Ops   │
                     └─────────┬─────────┘
                               │
                     ┌─────────▼─────────┐
                     │ Autonomous Ops    │
                     └───────────────────┘
