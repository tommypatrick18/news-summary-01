"""news-summary-01 entry (Python 3.13, standard library only).

Writes the summary in summary.txt beside this file to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The copy is byte-exact
and deterministic: two runs write identical bytes. Reads and writes
raw bytes so no newline or encoding translation can alter the text.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_bytes((HERE / "summary.txt").read_bytes())
