#!/usr/bin/env python3
"""Package every VCC component; stable archive metadata avoids maintenance dates."""
from pathlib import Path
import hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(s in {'.git','__pycache__','node_modules'} for s in p.relative_to(ROOT).parts) and p.name not in {'.DS_Store','vcc-complete.zip','SHA256SUMS.txt'})
manifest=''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n' for p in files)
(ROOT/'downloads/SHA256SUMS.txt').write_text(manifest)
archive=ROOT/'downloads/vcc-complete.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files+[ROOT/'downloads/SHA256SUMS.txt']:
  info=zipfile.ZipInfo('vcc/'+p.relative_to(ROOT).as_posix(),date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
  z.writestr(info,p.read_bytes())
print(f'Packaged {len(files)+1} files, {archive.stat().st_size:,} bytes')
