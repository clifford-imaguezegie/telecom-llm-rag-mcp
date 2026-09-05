#!/usr/bin/env python3
"""Validate the cleaned executed Module 4 master notebook before Git staging."""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, re, sys

EXPECTED_TOTAL_CELLS = 122
EXPECTED_CODE_CELLS = 39
EXPECTED_BENCHMARK_SHA = "c6160e33d5d2bd420ddffe7f820590c5becfa9521012d5373f06451bc9b44040"
EXPECTED_TITLE = "Module 4 — RAG + Knowledge-Based MCP Hybrid"

SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "Hugging Face token": re.compile(r"hf_[A-Za-z0-9]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "Bearer token": re.compile(r"Bearer\\s+[A-Za-z0-9._-]{20,}", re.I),
}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('notebook', nargs='?', default='notebooks/module_4/20_rag_mcp_hybrid.ipynb')
    args=ap.parse_args()
    path=Path(args.notebook)
    errors=[]; warnings=[]
    if not path.exists():
        print(f"FAIL: notebook not found: {path}")
        return 1
    try:
        nb=json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"FAIL: invalid notebook JSON: {e}")
        return 1
    cells=nb.get('cells',[])
    code=[c for c in cells if c.get('cell_type')=='code']
    md=[c for c in cells if c.get('cell_type')=='markdown']
    if len(cells)!=EXPECTED_TOTAL_CELLS: errors.append(f"cell count {len(cells)} != expected {EXPECTED_TOTAL_CELLS}")
    if len(code)!=EXPECTED_CODE_CELLS: errors.append(f"code cell count {len(code)} != expected {EXPECTED_CODE_CELLS}")
    if not md or EXPECTED_TITLE not in ''.join(md[0].get('source',[])): errors.append('expected Module 4 title missing from opening Markdown')
    if any(not c.get('outputs') for c in code): warnings.append('one or more code cells have no preserved outputs')
    # Every code cell should have Markdown immediately before and after in the cleaned edition.
    for i,c in enumerate(cells):
        if c.get('cell_type')=='code':
            if i==0 or cells[i-1].get('cell_type')!='markdown': errors.append(f'code cell at index {i} lacks preceding Markdown')
            if i==len(cells)-1 or cells[i+1].get('cell_type')!='markdown': errors.append(f'code cell at index {i} lacks following Markdown')
    whole=json.dumps(nb, ensure_ascii=False)
    if EXPECTED_BENCHMARK_SHA not in whole: errors.append('frozen benchmark SHA not found in notebook')
    if '47/48' not in whole and '47 / 48' not in whole: warnings.append('47/48 formal judge completion text not found')
    if 'Gemma Q16' not in whole: warnings.append('Gemma Q16 limitation text not found')
    for label,pat in SECRET_PATTERNS.items():
        if pat.search(whole): errors.append(f'possible embedded secret detected: {label}')
    print('='*88)
    print('MODULE 4 NOTEBOOK VALIDATION')
    print('='*88)
    print(f'Notebook        : {path}')
    print(f'SHA-256         : {sha256(path)}')
    print(f'Total cells     : {len(cells)}')
    print(f'Code cells      : {len(code)}')
    print(f'Markdown cells  : {len(md)}')
    print(f'Code with output: {sum(bool(c.get("outputs")) for c in code)}/{len(code)}')
    if warnings:
        print('\nWARNINGS:')
        for w in warnings: print(f'  - {w}')
    if errors:
        print('\nFAILURES:')
        for e in errors: print(f'  - {e}')
        print('\nSTATUS: FAIL')
        return 1
    print('\nSTATUS: PASS')
    print('Executed outputs remain present and the cleaned notebook structure is GitHub-ready.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
