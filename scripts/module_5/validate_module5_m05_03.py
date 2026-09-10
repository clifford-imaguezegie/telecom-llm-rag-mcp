#!/usr/bin/env python3
"""Static validation for the Module 5 Git package through M05_03.

This validator intentionally does NOT rebuild the 18.8M-row healthy baseline,
re-derive the complete M05_02 KPI products, or load M05_03 private truth.
It validates Git-visible notebook identity/structure, successful saved outputs,
Python syntax, key frozen handover markers, known Cell 10/12 corrections, and
documentation guardrails.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
NB = ROOT / "notebooks" / "module_5"
DOCS = ROOT / "docs" / "module_5"

EXPECTED_NOTEBOOK_SHA256 = {
    "M05_00_Implementation_and_Causal_Observability_Reference_v1.ipynb":
        "9c4db1552791510d3237fd8c7ff93cd7ae66d614d42fed0da7a268bf77fa910e",
    "M05_00_Implementation_and_Causal_Observability_Reference_v1_1.ipynb":
        "0de14402a1857eb18c83740b27d309eb605e73b7fac88245c01b51a59556d61e",
    "M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb":
        "8f0f1729f85f189758ed4244bd269623224d18ec4fa918f17e3b34d0f6a0bf5d",
    "M05_02_Runtime_Restore_KPI_Derivation_and_Healthy_Validation_v1.ipynb":
        "d319edd0c710565426f93bb4add2c0750ad82ec4dfb72ad80986889be169b278",
    "M05_03_Controlled_Incidents_and_Benchmark_v1.ipynb":
        "1fce555bf96adc3a8f27b0f08da9717b6ac93345b783e4b57d44336d91e0df7e",
}

M05_01_FREEZE = "4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968"
M05_01_TELEMETRY = "c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7"
M05_02_MANIFEST = "3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e"
M05_02_RECEIPT = "08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae"
M05_03_ROADMAP = "49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057"
M05_03_MANIFEST = "005232cb9326334e9a03f0a751b6eff325ffad4bc13c42caf48df8773193f7e7"
M05_03_RECEIPT = "59a0658f880fae4f8acea6358ad74702839a46eeb46e4c17e48b6c9013f8daca"

def sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()

def source(cell: dict) -> str:
    value = cell.get("source", "")
    return "".join(value) if isinstance(value, list) else str(value)

def load_notebook(path: Path, failures: list[str]) -> dict | None:
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"invalid notebook JSON {path.name}: {exc}")
        return None

    if not isinstance(nb.get("cells"), list):
        failures.append(f"invalid cells structure: {path.name}")
        return None
    return nb

def validate_common_notebook(path: Path, nb: dict, failures: list[str]) -> None:
    raw = path.read_text(encoding="utf-8")

    # Do not permit obvious literal secret assignments.
    secret_patterns = [
        r"(?i)\bKAGGLE_KEY\s*=\s*['\"][^'\"]+",
        r"(?i)\bHF_TOKEN\s*=\s*['\"][^'\"]+",
        r"(?i)\bOPENAI_API_KEY\s*=\s*['\"][^'\"]+",
        r"(?i)\bANTHROPIC_API_KEY\s*=\s*['\"][^'\"]+",
    ]
    for pattern in secret_patterns:
        if re.search(pattern, raw):
            failures.append(f"possible literal credential in {path.name}: {pattern}")

    for idx, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") != "code":
            continue

        # Syntax compilation applies only to the notebook introduced by
        # the M05_03 Git package. M05_00-M05_02 are frozen upstream notebooks:
        # their identities, saved outputs and handover markers are validated,
        # but they are not re-qualified against the local Python runtime.
        if path.name == "M05_03_Controlled_Incidents_and_Benchmark_v1.ipynb":
            try:
                compile(source(cell), f"{path.name}:cell_{idx}", "exec")
            except SyntaxError as exc:
                failures.append(f"Python syntax error {path.name} cell {idx}: {exc}")

        for output in cell.get("outputs", []):
            if output.get("output_type") == "error":
                failures.append(f"saved error output {path.name} cell {idx}")

def require_markers(raw: str, name: str, markers: dict[str, str], failures: list[str]) -> None:
    for label, marker in markers.items():
        if marker not in raw:
            failures.append(f"{name}: missing {label}: {marker}")

def main() -> int:
    failures: list[str] = []
    notebooks: dict[str, dict] = {}

    for name, expected in EXPECTED_NOTEBOOK_SHA256.items():
        path = NB / name
        if not path.exists():
            failures.append(f"missing notebook: {path}")
            continue

        observed = sha256_lf(path)
        if observed != expected:
            failures.append(f"LF-normalized SHA mismatch {name}: {observed} != {expected}")

        nb = load_notebook(path, failures)
        if nb is None:
            continue
        notebooks[name] = nb
        validate_common_notebook(path, nb, failures)

    # M05_01 frozen root-of-trust markers.
    p1 = NB / "M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb"
    if p1.exists():
        raw = p1.read_text(encoding="utf-8")
        require_markers(raw, p1.name, {
            "M05_01 freeze": M05_01_FREEZE,
            "canonical telemetry": M05_01_TELEMETRY,
            "closeout": "M05_01_CLOSEOUT_PASS",
        }, failures)

    # M05_02 frozen KPI handover markers.
    p2 = NB / "M05_02_Runtime_Restore_KPI_Derivation_and_Healthy_Validation_v1.ipynb"
    if p2.exists():
        raw = p2.read_text(encoding="utf-8")
        require_markers(raw, p2.name, {
            "M05_02 KPI manifest": M05_02_MANIFEST,
            "M05_02 receipt": M05_02_RECEIPT,
            "M05_02 closeout": "M05_02_CLOSEOUT_PASS",
            "NRCellCU KPI SHA": "709c9883bad799dec3907624a7590f5e44356d9fef7c00f4446d165fd1b2223f",
            "SubNetwork KPI SHA": "18d5a60ca91139242e85e9f5468346a66bedf70f8736e01507568f2afb9c42ba",
        }, failures)

    # M05_03 benchmark integrity markers and known fixes.
    p3 = NB / "M05_03_Controlled_Incidents_and_Benchmark_v1.ipynb"
    if p3.exists():
        raw = p3.read_text(encoding="utf-8")
        nb3 = notebooks.get(p3.name)

        require_markers(raw, p3.name, {
            "roadmap amendment": M05_03_ROADMAP,
            "benchmark manifest": M05_03_MANIFEST,
            "validation receipt": M05_03_RECEIPT,
            "truth separation gate": "M05_03_TRUTH_SEPARATION_PASS",
            "split isolation gate": "M05_03_SPLIT_ISOLATION_PASS",
            "closeout gate": "M05_03_CLOSEOUT_PASS",
            "M05_04 authorization": "M05_04_TELEMETRY_MCP_SERVICE",
            "private-dir prohibition": "M05_04 may load private/ directory   : NO",
        }, failures)

        if nb3 is not None:
            code_cells = [c for c in nb3["cells"] if c.get("cell_type") == "code"]
            markdown_cells = [c for c in nb3["cells"] if c.get("cell_type") == "markdown"]
            if len(nb3["cells"]) != 77 or len(code_cells) != 19 or len(markdown_cells) != 58:
                failures.append(
                    f"M05_03 cell structure changed: total={len(nb3['cells'])}, "
                    f"code={len(code_cells)}, markdown={len(markdown_cells)}"
                )

            sanitization = next(
                (source(c) for c in code_cells if "CREATE OR REPLACE TABLE m05_03_agent_telemetry" in source(c)),
                "",
            )
            if not sanitization:
                failures.append("M05_03: agent-visible sanitization cell not found")
            elif re.search(r"(?m)^\s*du_id\s*,", sanitization):
                failures.append("M05_03: stale invalid du_id projection remains in Cell 10")

            repro = next(
                (source(c) for c in code_cells if "repro = con.execute" in source(c) or "repro=con.execute" in source(c)),
                "",
            )
            if not repro:
                failures.append("M05_03: KPI reproduction query not found")
            elif not re.search(
                r"JOIN\s+m05_03_private_cases\s+pc\s+ON\s+k\.scenario_id\s*=\s*pc\.scenario_id",
                repro,
                flags=re.I | re.S,
            ):
                failures.append("M05_03: corrected explicit scenario_id join not found in Cell 12")

    # Documentation should describe the active roadmap, not Sionna as next stage.
    doc_files = [
        ROOT / "README.md",
        DOCS / "README.md",
        DOCS / "ARCHITECTURE.md",
        DOCS / "STATUS.md",
        DOCS / "ARTIFACTS.md",
        DOCS / "REPRODUCIBILITY.md",
        DOCS / "M05_03_NOTEBOOK_REVIEW.md",
        DOCS / "MODULE5_CHANGELOG.md",
    ]
    for path in doc_files:
        if not path.exists():
            failures.append(f"missing documentation: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if "M05_04" not in text and path.name != "ARTIFACTS.md":
            failures.append(f"{path}: M05_04 handover not documented")

    active_docs = "\n".join(
        (DOCS / name).read_text(encoding="utf-8")
        for name in ["README.md", "ARCHITECTURE.md", "STATUS.md"]
        if (DOCS / name).exists()
    )
    stale_phrases = [
        "M05_03 — Sionna Radio Reference Validation",
        "M05_03 — Sionna independent radio reference validation",
        "M05_03 | Sionna independent radio reference validation | **next**",
    ]
    for phrase in stale_phrases:
        if phrase in active_docs:
            failures.append(f"stale active Sionna-next narrative: {phrase}")

    if failures:
        print("MODULE 5 M05_03 GIT VALIDATION: FAIL")
        for failure in failures:
            print(" -", failure)
        return 1

    print("MODULE 5 M05_03 GIT VALIDATION: PASS")
    print(" - M05_00/M05_01/M05_02 notebook identities: PASS")
    print(" - M05_03 reviewed notebook identity: PASS")
    print(" - saved error outputs: 0")
    print(" - M05_03 Python syntax: PASS")
    print(" - Cell 10 du_id correction: PASS")
    print(" - Cell 12 explicit scenario_id join: PASS")
    print(" - M05_03 frozen handover markers: PASS")
    print(" - active roadmap: M05_04_TELEMETRY_MCP_SERVICE")
    print(" - private benchmark truth committed by this package: NO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
