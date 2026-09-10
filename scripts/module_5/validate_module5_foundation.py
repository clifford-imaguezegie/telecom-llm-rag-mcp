#!/usr/bin/env python3
"""Static validation for the Module 5 M05_01 Git package.

This validator does not rebuild the 18.8M-row telemetry dataset. It checks
Git-visible notebook identities, notebook structure, authoritative M05_01
V1.2/V1.1 handover markers, control-cell ordering, Python syntax, absence of
saved error outputs, and absence of embedded Kaggle credentials.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
NB = ROOT / "notebooks" / "module_5"

EXPECTED = {
    "M05_00_Implementation_and_Causal_Observability_Reference_v1.ipynb":
        "9c4db1552791510d3237fd8c7ff93cd7ae66d614d42fed0da7a268bf77fa910e",
    "M05_00_Implementation_and_Causal_Observability_Reference_v1_1.ipynb":
        "0de14402a1857eb18c83740b27d309eb605e73b7fac88245c01b51a59556d61e",
    "M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb":
        "8f0f1729f85f189758ed4244bd269623224d18ec4fa918f17e3b34d0f6a0bf5d",
}

FREEZE_SEMANTIC_SHA = "4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968"
FOUNDATION_RECONCILIATION_SHA = "8366a6e8bee9ddfdbcc665a668caac50e1bba86c02730f48277250206279e4d9"
BUNDLE_INDEX_SEMANTIC_SHA = "55c8ef51f905945fb825fad3bb35b932ccf7e140f5ffe9d85d3430071ff7143b"
FOUNDATION_PERSISTENCE_SHA = "936b605cb1ce3c2d2b2977fed537df65c5e61e19e26ff655f89b27b919d62879"
TELEMETRY_QUALIFICATION_SHA = "fc3c38f980209b1d5a9504b30f98efa6636ba7eedc153ef4f4d1e7bb49be156a"
CANONICAL_MANIFEST_SHA = "e856ffe3f7ed97e6ad4592e999e5fd3adf5993f80ac72cdada1f374ab6543411"
CANONICAL_DATASET_SHA = "c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7"

FOUNDATION_DRIVE_PATH = (
    "/content/drive/MyDrive/Telecom_AI_Engineering_Platform/"
    "Module_5/M05_01/foundation/foundation_bundle_v1_2"
)

TELEMETRY_DRIVE_PATH = (
    "/content/drive/MyDrive/Telecom_AI_Engineering_Platform/"
    "Module_5/M05_01/telemetry/healthy_baseline_v1_1"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_lf_normalized(path: Path) -> str:
    """Portable notebook identity across LF/CRLF Git checkouts."""
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def main() -> int:
    failures: list[str] = []

    # --------------------------------------------------------
    # Portable Git notebook identities (normalize CRLF -> LF)
    # --------------------------------------------------------
    for name, expected in EXPECTED.items():
        path = NB / name

        if not path.exists():
            failures.append(f"missing notebook: {path}")
            continue

        observed = sha256_lf_normalized(path)
        if observed != expected:
            failures.append(
                f"LF-normalized SHA mismatch {name}: {observed} != {expected}"
            )

        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"invalid notebook JSON {name}: {exc}")
            continue

        if "cells" not in notebook or not isinstance(notebook["cells"], list):
            failures.append(f"invalid cells structure: {name}")

        raw = path.read_text(encoding="utf-8")
        for forbidden in ["KAGGLE_USERNAME=", "KAGGLE_KEY="]:
            if forbidden in raw:
                failures.append(
                    f"possible embedded credential marker in {name}: {forbidden}"
                )

    # --------------------------------------------------------
    # M05_01 structural / semantic handover checks
    # --------------------------------------------------------
    m05_01 = NB / "M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb"

    if m05_01.exists():
        notebook = json.loads(m05_01.read_text(encoding="utf-8"))
        raw = m05_01.read_text(encoding="utf-8")

        required_markers = {
            "M05_01 freeze V1.2 semantic SHA": FREEZE_SEMANTIC_SHA,
            "foundation reconciliation SHA": FOUNDATION_RECONCILIATION_SHA,
            "bundle index semantic SHA": BUNDLE_INDEX_SEMANTIC_SHA,
            "foundation persistence SHA": FOUNDATION_PERSISTENCE_SHA,
            "telemetry qualification SHA": TELEMETRY_QUALIFICATION_SHA,
            "canonical manifest SHA": CANONICAL_MANIFEST_SHA,
            "canonical dataset SHA": CANONICAL_DATASET_SHA,
            "M05_01 closeout marker": "M05_01_CLOSEOUT_PASS",
            "V1.2 freeze marker": "M05_01_FREEZE_V1_2_PASS",
            "Google Drive persistence marker": "GOOGLE_DRIVE_PERSISTENCE_PASS",
            "foundation Drive restore path": FOUNDATION_DRIVE_PATH,
            "telemetry Drive restore path": TELEMETRY_DRIVE_PATH,
        }

        for label, marker in required_markers.items():
            if marker not in raw:
                failures.append(f"missing M05_01 marker: {label}")

        # Saved Git copy should not contain traceback/error output.
        for index, cell in enumerate(notebook["cells"]):
            if cell.get("cell_type") != "code":
                continue

            if cell.get("execution_count") is not None:
                failures.append(
                    f"Git-clean execution_count should be null: cell index {index}"
                )

            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    failures.append(
                        f"saved error output present: cell index {index}"
                    )

            try:
                compile(cell_source(cell), f"cell_{index}", "exec")
            except SyntaxError as exc:
                failures.append(
                    f"Python syntax error in cell index {index}: {exc}"
                )

        # Table-of-contents links must resolve to notebook anchors.
        markdown = "\n".join(
            cell_source(cell)
            for cell in notebook["cells"]
            if cell.get("cell_type") == "markdown"
        )

        import re

        anchors = set(
            re.findall(r'<a id="([^"]+)"></a>', markdown)
        )

        toc_cell = next(
            (
                cell_source(cell)
                for cell in notebook["cells"]
                if cell.get("cell_type") == "markdown"
                and '<a id="notebook-navigation"></a>' in cell_source(cell)
            ),
            "",
        )

        toc_links = re.findall(r'\]\(#([^)]+)\)', toc_cell)

        for anchor in toc_links:
            if anchor not in anchors:
                failures.append(
                    f"unresolved notebook TOC anchor: {anchor}"
                )

        # The corrective lineage must be executable in dependency order.
        control_anchors = [
            "cell-20-telemetry-supersession-reconciliation",
            "cell-21-initial-freeze-v1-1",
            "cell-20a-foundation-identity-reconciliation",
            "cell-21a-corrected-freeze-v1-2",
            "cell-22-foundation-bundle-v1-2",
        ]

        anchor_positions: dict[str, int] = {}

        for index, cell in enumerate(notebook["cells"]):
            if cell.get("cell_type") != "markdown":
                continue
            source = cell_source(cell)
            for anchor in control_anchors:
                if f'<a id="{anchor}"></a>' in source:
                    anchor_positions[anchor] = index

        if set(anchor_positions) != set(control_anchors):
            missing = sorted(set(control_anchors) - set(anchor_positions))
            failures.append(
                f"missing control-lineage anchors: {missing}"
            )
        else:
            positions = [anchor_positions[a] for a in control_anchors]
            if positions != sorted(positions):
                failures.append(
                    "control-lineage cell order is not executable top-to-bottom"
                )

        # Active notebook narrative must not point M05_02 at old Kaggle V1 sources.
        markdown_only = markdown

        forbidden_active_phrases = [
            "M05_02 should restore M05_01 from **two durable private Kaggle sources**",
            "proceed to EDA",
            "return to Cell 13 and rerun",
        ]

        for phrase in forbidden_active_phrases:
            if phrase in markdown_only:
                failures.append(
                    f"stale active notebook narrative found: {phrase}"
                )

    if failures:
        print("MODULE 5 FOUNDATION VALIDATION: FAIL")
        for failure in failures:
            print(" -", failure)
        return 1

    print("MODULE 5 FOUNDATION VALIDATION: PASS")
    for name, expected in EXPECTED.items():
        print(f" - {name}: {expected} (LF-normalized)")

    print(f" - M05_01 freeze V1.2 semantic SHA: {FREEZE_SEMANTIC_SHA}")
    print(f" - foundation reconciliation SHA: {FOUNDATION_RECONCILIATION_SHA}")
    print(f" - bundle index semantic SHA: {BUNDLE_INDEX_SEMANTIC_SHA}")
    print(f" - foundation persistence SHA: {FOUNDATION_PERSISTENCE_SHA}")
    print(f" - telemetry qualification SHA: {TELEMETRY_QUALIFICATION_SHA}")
    print(f" - canonical telemetry semantic SHA: {CANONICAL_DATASET_SHA}")
    print(" - saved error outputs: 0")
    print(" - control-lineage order: PASS")
    print(" - Google Drive restore contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
