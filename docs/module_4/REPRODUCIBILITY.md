# Reproducibility

## Frozen experiment identifiers

| Item | Value |
|---|---|
| Benchmark version | `module4_hybrid_eval_v1` |
| Benchmark SHA-256 | `c6160e33d5d2bd420ddffe7f820590c5becfa9521012d5373f06451bc9b44040` |
| Judge rubric SHA-256 | `45d273ca621000ea43e208b233e25b906049de2f57601b9062b130b99e4f1809` |
| Granite formal config SHA-256 | `4e135615780eccd7f7f140c1fb35af55569924ced99a4a87d28c2c2de2413742` |

## Generator model revisions

### Gemma 4 12B

- Model: `google/gemma-4-12B-it-qat-w4a16-ct`
- Revision: `1d2c2d7f2466070e69d6fb3fd5ce9a7d75f2f6ee`
- Deployment: QAT W4A16 / compressed tensors

### Qwen3.8 27B

- Model: `Qwen/Qwen3.8-27B`
- Revision: `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`
- Source: official BF16
- Formal runtime: BitsAndBytes INT4
- Thinking: disabled
- vLLM: `0.28.0`
- BitsAndBytes: `0.50.2`
- vLLM BnB plugin: `0.0.2`

### Qwen3.5 9B

- Model: `Qwen/Qwen3.5-9B`
- Revision: `c202236235762e1c871ad0ccb60c8ee5ba337b9a`
- Source: official BF16
- Formal runtime: BitsAndBytes INT4
- Thinking: disabled

## Independent judge

- Model: `ibm-granite/granite-4.2-8b`
- Revision: `7fce579a7fbbad4b1e7703b6850cefd517a4002b`
- Precision: BF16
- Thinking: standard/default
- Reasoning parser: `nemotron_v3`
- Temperature: `1.0`
- Top-p: `0.95`
- Formal max model length: `20,480`
- Formal max output tokens: `12,288`
- GPU memory utilization: `0.97`
- Max concurrent sequences: `1`
- BGE-M3 during judging: CPU

## Retrieval controls

- RAG top-k: `5`
- MCP top-k: `5`
- maximum retrieval rounds: `3`
- maximum presented evidence: `5`
- maximum evidence chars/item: `2,500`
- maximum final context chars: `12,500`
- Hybrid execution: concurrent
- Hybrid query policy: same query to both branches
- RRF k: `60`
- near-duplicate threshold: `0.88`

## Formal generator artifact hashes used by Granite

| Generator | SHA-256 |
|---|---|
| Gemma 4 12B | `155508e7e8d927a5c84c23fed14d57028736a8e32c369c4b41a57aa363b81a22` |
| Qwen3.8 27B | `8d63f6e268fcd9c055b7f80c8de7d8fab4dbe3b0f1e1ed920ee5afd3c11823d3` |
| Qwen3.5 9B | `6d29bc5fd3e1455613c6255dc8a0c73a49fa0d58cf2adcbcba6109eb2e49eace` |

## Runtime notes

The executed notebook was developed in Google Colab with an NVIDIA L4 GPU. Runtime conditions changed across model stages because the three generators have different memory requirements.

Do not assume that a fresh runtime can reproduce the experiment merely by rerunning every cell with arbitrary current package versions.

For best reproducibility:

1. use the pinned model revisions;
2. preserve the frozen benchmark/config files under `results/module_4/frozen_benchmark/`;
3. use the formal manifests under `results/module_4/formal_runs/`;
4. restore the frozen RAG/MCP artifacts rather than rebuilding them;
5. preserve all formal failures rather than retrying until success;
6. keep the Granite judge blind to generator identity and operational metadata.

## Analysis-only reproduction

The deterministic results can be inspected without loading any LLM.

Install:

```bash
pip install -r requirements/module_4_analysis.txt
```

Then use the CSV/JSON artifacts in `results/module_4/final_analysis/`.

The cleaned notebook contains the executed Cell 12D/13 analysis and preserved outputs.

## External full archive

The GitHub package intentionally excludes redundant checkpoints and server logs.

The complete experimental archive was separately persisted to:

- Google Drive as a timestamped ZIP;
- Kaggle dataset slug: `cliffordimaguezegie/telecom-ai-module-4-outputs`.

The Kaggle dataset was private at the time of archival.
