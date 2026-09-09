#!/usr/bin/env python3
"""Static validation for the Module 5 foundation Git package.

This validator does not reproduce the large telemetry dataset. It checks
the committed notebook identities, basic notebook structure, expected
M05_01 freeze markers, and absence of embedded Kaggle credentials.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
NB = ROOT / "notebooks" / "module_5"

EXPECTED = {
    "M05_00_Implementation_and_Causal_Observability_Reference_v1.ipynb": "9c4db1552791510d3237fd8c7ff93cd7ae66d614d42fed0da7a268bf77fa910e",
    "M05_00_Implementation_and_Causal_Observability_Reference_v1_1.ipynb": "0de14402a1857eb18c83740b27d309eb605e73b7fac88245c01b51a59556d61e",
    "M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb": "8e80bfe13c2fd2eae4a10dd42df273f183dc9b666818c7b33838e69a7b7f526b",
}

FREEZE_SEMANTIC_SHA = "3a519602da5e211df684786441c41669fbfdaac1c0d13254d18187ad5ce874e8"
FOUNDATION_PERSISTENCE_SHA = "fb4815ad27a88951b4b5f4d14a942510e07191aeb366929fcfec3701fee20413"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main() -> int:
    failures = []
    for name, expected in EXPECTED.items():
        path = NB / name
        if not path.exists():
            failures.append(f"missing notebook: {path}")
            continue
        observed = sha256(path)
        if observed != expected:
            failures.append(f"SHA mismatch {name}: {observed} != {expected}")
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"invalid notebook JSON {name}: {exc}")
            continue
        if "cells" not in nb or not isinstance(nb["cells"], list):
            failures.append(f"invalid cells structure: {name}")
        raw = path.read_text(encoding="utf-8")
        for forbidden in ["KAGGLE_USERNAME=", "KAGGLE_KEY="]:
            if forbidden in raw:
                failures.append(f"possible embedded credential marker in {name}: {forbidden}")

    m05_01 = NB / "M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb"
    if m05_01.exists():
        raw = m05_01.read_text(encoding="utf-8")
        if FREEZE_SEMANTIC_SHA not in raw:
            failures.append("M05_01 freeze semantic SHA marker not found")
        if FOUNDATION_PERSISTENCE_SHA not in raw:
            failures.append("M05_01 foundation persistence semantic SHA marker not found")
        if "M05_01_FREEZE_PASS" not in raw:
            failures.append("M05_01 freeze decision marker not found")
        if "FOUNDATION_PERSISTENCE_PASS" not in raw:
            failures.append("Cell 18 persistence decision marker not found")

    if failures:
        print("MODULE 5 FOUNDATION VALIDATION: FAIL")
        for f in failures:
            print(" -", f)
        return 1

    print("MODULE 5 FOUNDATION VALIDATION: PASS")
    for name, expected in EXPECTED.items():
        print(f" - {name}: {expected}")
    print(f" - freeze semantic SHA: {FREEZE_SEMANTIC_SHA}")
    print(f" - foundation persistence semantic SHA: {FOUNDATION_PERSISTENCE_SHA}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
