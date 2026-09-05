# Module 4 GitHub Integration Checklist

This package is an **overlay** for the existing `telecom-llm-rag-mcp` repository. Extract/copy it at the repository root while on branch `module-4-rag-mcp`.

## Expected additions

```text
notebooks/module_4/20_rag_mcp_hybrid.ipynb
docs/module_4/
results/module_4/
requirements/module_4_runtime.txt
requirements/module_4_analysis.txt
scripts/module_4/validate_module4_notebook.py
.gitattributes
```

The package intentionally does **not** contain a root `README.md` or `.gitignore`, so it cannot overwrite the repository's existing files.

## Before staging

- [ ] Confirm active branch is `module-4-rag-mcp`.
- [ ] Copy/extract the overlay at repository root.
- [ ] Merge the separately supplied Module 4 root-README insert into the existing root `README.md`.
- [ ] Review existing `.gitignore` and add the Module 4 runtime/archive patterns if not already present.
- [ ] Run `python scripts/module_4/validate_module4_notebook.py`.
- [ ] Run `tree /F` and verify Module 1–3 files remain unchanged.
- [ ] Check largest files before `git add`.

## Recommended PowerShell checks

```powershell
git branch
git status
tree /F
python .\scripts\module_4\validate_module4_notebook.py
Get-ChildItem -Recurse | Sort-Object Length -Descending |
    Select-Object -First 20 FullName, Length
git status --short
```

## Do not commit

- complete Google Drive/Kaggle ZIP archives;
- Colab runtime directories;
- checkpoints not included in the curated package;
- vLLM server logs;
- model weights/caches;
- Kaggle credentials or other secrets.

## Commit boundary

Only after the structure and validator pass:

```powershell
git add notebooks/module_4 docs/module_4 results/module_4 requirements/module_4_runtime.txt requirements/module_4_analysis.txt scripts/module_4 .gitattributes README.md .gitignore
git status
git diff --cached --stat
```

Review the staged diff before committing.
