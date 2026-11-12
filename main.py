import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, 'summary.txt')

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'entry.txt')

with open(input_path, 'rb') as f_src:
    content = f_src.read()

with open(output_path, 'wb') as f_dst:
    f_dst.write(content)
