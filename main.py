import os
from pathlib import Path

def main():
    src_dir = Path(__file__).parent
    src_path = src_dir / "summary.txt"
    
    out_dir_path = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir_path.mkdir(parents=True, exist_ok=True)
    
    dst_path = out_dir_path / "entry.txt"
    
    data = src_path.read_bytes()
    dst_path.write_bytes(data)

if __name__ == "__main__":
    main()