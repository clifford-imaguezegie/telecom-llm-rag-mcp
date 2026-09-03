from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "notebooks" / "module_2"
BENCHMARK_DIR = ROOT / "benchmarks" / "module_1_2"
RESULT_DIR = ROOT / "results" / "module_2" / "public_results"

EXPECTED_NOTEBOOKS = [
    "02_rag_stage_1.ipynb",
    "03_essentialai_rag_v1.ipynb",
    "04_essentialai_only.ipynb",
    "05_otel2_only.ipynb",
    "06_gemma4_only.ipynb",
    "07_gemma4_rag_v1.ipynb",
    "08_rag_evaluation.ipynb",
]

EXPECTED_RESULTS = [
    "track1_essential_ai_only.json",
    "track1_essential_ai_plus_rag.json",
    "track1_gemma_4_only.json",
    "track1_gemma_4_plus_rag.json",
    "track1_otel_2_0_only.json",
    "track2_essential_ai_only.json",
    "track2_essential_ai_plus_rag.json",
    "track2_gemma_4_only.json",
    "track2_gemma_4_plus_rag.json",
    "track2_otel_2_0_only.json",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"hf_[A-Za-z0-9]{15,}"),
]

def canonical_sha(obj):
    payload = json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def main():
    missing_nb = [n for n in EXPECTED_NOTEBOOKS if not (NOTEBOOK_DIR / n).exists()]
    if missing_nb:
        raise SystemExit(f"FAIL: missing Module 2 notebooks: {missing_nb}")

    found_nb = sorted(p.name for p in NOTEBOOK_DIR.glob("*.ipynb"))
    if found_nb != EXPECTED_NOTEBOOKS:
        raise SystemExit(f"FAIL: unexpected Module 2 notebook set: {found_nb}")

    error_outputs = []
    secret_hits = []
    stale_module_labels = []

    for name in EXPECTED_NOTEBOOKS:
        data = json.loads((NOTEBOOK_DIR / name).read_text(encoding="utf-8"))
        cells = data.get("cells", [])
        if not cells:
            raise SystemExit(f"FAIL: {name} contains no cells.")

        source = "\n".join(
            "".join(cell.get("source", []))
            if isinstance(cell.get("source"), list)
            else str(cell.get("source", ""))
            for cell in cells
        )

        for pattern in SECRET_PATTERNS:
            if pattern.search(source):
                secret_hits.append((name, pattern.pattern))

        if re.search(r"\bMODULE [456]\.", source):
            stale_module_labels.append(name)

        if ":contentReference[" in source or "oaicite" in source:
            raise SystemExit(f"FAIL: stale generated citation marker found in {name}")

        for idx, cell in enumerate(cells):
            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    error_outputs.append(
                        (name, idx, output.get("ename"), output.get("evalue"))
                    )

    if secret_hits:
        raise SystemExit(f"FAIL: possible literal secrets found: {secret_hits}")
    if stale_module_labels:
        raise SystemExit(
            f"FAIL: project-conflicting MODULE 4/5/6 labels remain: {stale_module_labels}"
        )
    if error_outputs:
        raise SystemExit(f"FAIL: saved error outputs found: {error_outputs}")

    track1 = json.loads(
        (BENCHMARK_DIR / "track1_custom_20_questions.json").read_text(encoding="utf-8")
    )
    track2 = json.loads(
        (BENCHMARK_DIR / "track2_industry_32_questions.json").read_text(encoding="utf-8")
    )
    if len(track1) != 20 or len(track2) != 32:
        raise SystemExit("FAIL: benchmark question counts are not 20 / 32.")

    result_files = sorted(p.name for p in RESULT_DIR.glob("*.json"))
    if result_files != EXPECTED_RESULTS:
        raise SystemExit(f"FAIL: unexpected public result set: {result_files}")

    t1sha = canonical_sha(track1)
    t2sha = canonical_sha(track2)

    for name in EXPECTED_RESULTS:
        data = json.loads((RESULT_DIR / name).read_text(encoding="utf-8"))
        metadata = data.get("metadata", {})
        results = data.get("results", [])
        expected_n = 20 if metadata.get("track") == "Track 1" else 32
        expected_sha = t1sha if expected_n == 20 else t2sha

        if len(results) != expected_n:
            raise SystemExit(f"FAIL: {name} has {len(results)} results, expected {expected_n}.")
        if metadata.get("benchmark_sha256") != expected_sha:
            raise SystemExit(f"FAIL: benchmark SHA mismatch in {name}")

        for record in results:
            retrieval = record.get("retrieval")
            if isinstance(retrieval, dict):
                for evidence in retrieval.get("results", []) or []:
                    if "text" in evidence or "path" in evidence:
                        raise SystemExit(
                            f"FAIL: unsanitized retrieval evidence found in {name}"
                        )

    print(f"Validated {len(EXPECTED_NOTEBOOKS)} Module 2 notebooks.")
    print(f"Validated {len(EXPECTED_RESULTS)} normalized public result files.")
    print("PASS: notebooks, benchmarks, public results and basic secret/hygiene checks passed.")

if __name__ == "__main__":
    main()
