import os
from pathlib import Path

def main():
    source_path = Path(__file__).resolve().parent / "summary.txt"
    
    target_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target_dir = Path(target_dir_name)
    target_dir.mkdir(parents=True, exist_ok=True)
    
    target_path = target_dir / "entry.txt"
    target_path.write_bytes(source_path.read_bytes())

if __name__ == "__main__":
    main()