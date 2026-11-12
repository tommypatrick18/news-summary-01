import os
from pathlib import Path

def main():
    source_path = Path(__file__).resolve().parent / "summary.txt"
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_env)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    target_path = output_dir / "entry.txt"
    
    data = source_path.read_bytes()
    target_path.write_bytes(data)

if __name__ == "__main__":
    main()