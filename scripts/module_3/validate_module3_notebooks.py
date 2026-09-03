from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[2]
nb_dir=ROOT/'notebooks'/'module_3'
expected=[f'{i:02d}_' for i in range(9,20)]
files=sorted(nb_dir.glob('*.ipynb'))
errors=[]
for p in files:
    try: nb=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{p.name}: invalid JSON: {e}'); continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    if re.search(r'sk-[A-Za-z0-9_-]{10,}', text): errors.append(f'{p.name}: possible literal API key')
    if re.search(r'[A-Z]:\\\\Users\\\\', text): errors.append(f'{p.name}: absolute Windows user path')
print(f'Validated {len(files)} Module 3 notebooks.')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print('PASS: notebook JSON and basic secret/path hygiene checks passed.')
