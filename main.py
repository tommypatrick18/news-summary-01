import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "summary.txt")

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

with open(input_path, "rb") as f_in:
    data = f_in.read()

with open(output_path, "wb") as f_out:
    f_out.write(data)
