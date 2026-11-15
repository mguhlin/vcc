#!/usr/bin/env python3
"""Verify the public manifest and ZIP against the actual shipped source tree."""
import hashlib
import zipfile
from pathlib import Path
from project_files import public_files

ROOT=Path(__file__).resolve().parents[1]
files={path.relative_to(ROOT).as_posix():path.read_bytes() for path in public_files(ROOT)}
expected=''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n' for name,data in files.items())
manifest=(ROOT/'downloads/SHA256SUMS.txt').read_bytes()
if manifest.decode()!=expected:raise SystemExit('Checksum manifest is stale; run scripts/package.py')
files['downloads/SHA256SUMS.txt']=manifest
with zipfile.ZipFile(ROOT/'downloads/vcc-complete.zip') as archive:
    names=archive.namelist()
    if len(names)!=len(set(names)) or set(names)!={'vcc/'+name for name in files}:raise SystemExit('Complete ZIP has missing, duplicate, or unexpected components')
    for name,data in files.items():
        if archive.read('vcc/'+name)!=data:raise SystemExit(f'Complete ZIP contains a stale component: {name}')
print(f'Verified {len(files)} complete-bundle components and their checksums')
