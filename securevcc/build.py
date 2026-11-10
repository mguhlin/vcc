#!/usr/bin/env python3
"""The VCC root builder now renders the complete SecureVCC guide."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1]/'scripts/build.py'),run_name='__main__')
