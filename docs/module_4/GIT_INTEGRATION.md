# Git Integration Notes

## `.gitattributes`

The overlay adds a root `.gitattributes` because the current repository tree supplied for review did not contain one.

```gitattributes
*.ipynb linguist-language=Python
*.png binary
*.zip binary
```

## `.gitignore`

The existing repository already has a root `.gitignore`, so the overlay deliberately does not replace it. Merge any missing patterns below into the existing file:

```gitignore
.env
.env.*
kaggle.json
**/kaggle.json
*.pem
*.key
__pycache__/
*.py[cod]
.ipynb_checkpoints/
.venv/
venv/
.cache/
huggingface/
models/
*.safetensors
*.gguf
*.bin
*.pt
*.pth
*.faiss
*.duckdb
*.db
*.log
tmp/
temp/
module4_runtime/
module4_kaggle_publish/
module4_complete_artifacts_*.zip
.DS_Store
Thumbs.db
.vscode/
.idea/
```

Do not remove existing ignore rules from the repository.
