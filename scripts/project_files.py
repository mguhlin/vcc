"""The public distribution boundary shared by packaging and verification."""
from pathlib import Path

LOCAL_DIRS={'.git','__pycache__','node_modules','.venv','venv','.pytest_cache','.mypy_cache','.cache'}
OUTPUTS={'downloads/vcc-complete.zip','downloads/SHA256SUMS.txt'}


def public_files(root):
    files=[]
    for path in Path(root).rglob('*'):
        relative=path.relative_to(root)
        if not path.is_file() or any(part in LOCAL_DIRS for part in relative.parts):continue
        if path.name=='.DS_Store' or path.suffix=='.pyc' or relative.as_posix() in OUTPUTS:continue
        # Local environment files never belong in the public download.
        if (path.name=='.env' or path.name.startswith('.env.')) and path.name not in {'.env.example','.env.sample'}:continue
        if path.is_symlink():raise ValueError(f'Public component must not be a symlink: {relative}')
        files.append(path)
    return sorted(files)
