import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
input_file = script_dir / "summary.txt"

output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_dir = Path(output_dir_env)
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.txt"

output_file.write_bytes(input_file.read_bytes())