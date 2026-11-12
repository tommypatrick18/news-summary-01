import os
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    source_path = script_dir / "summary.txt"

    output_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target_dir = Path(output_env)
    target_path = target_dir / "entry.txt"

    target_dir.mkdir(parents=True, exist_ok=True)

    data = source_path.read_bytes()
    target_path.write_bytes(data)

if __name__ == "__main__":
    main()