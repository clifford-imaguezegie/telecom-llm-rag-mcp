from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "notebooks" / "module_1"

EXPECTED = ["01_llm_base.ipynb"]
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"hf_[A-Za-z0-9]{15,}"),
]

def main():
    missing = [name for name in EXPECTED if not (NOTEBOOK_DIR / name).exists()]
    if missing:
        raise SystemExit(f"FAIL: missing Module 1 notebooks: {missing}")

    found = sorted(p.name for p in NOTEBOOK_DIR.glob("*.ipynb"))
    if found != EXPECTED:
        raise SystemExit(f"FAIL: unexpected Module 1 notebook set: {found}")

    error_outputs = []
    secret_hits = []

    for name in EXPECTED:
        path = NOTEBOOK_DIR / name
        data = json.loads(path.read_text(encoding="utf-8"))
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

        for idx, cell in enumerate(cells):
            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    error_outputs.append(
                        (name, idx, output.get("ename"), output.get("evalue"))
                    )

    if secret_hits:
        raise SystemExit(f"FAIL: possible literal secrets found: {secret_hits}")
    if error_outputs:
        raise SystemExit(f"FAIL: saved error outputs found: {error_outputs}")

    print(f"Validated {len(EXPECTED)} Module 1 notebook.")
    print("PASS: notebook JSON, expected file set, error-output and basic secret checks passed.")

if __name__ == "__main__":
    main()
