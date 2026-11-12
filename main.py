"""
This module reads summary.txt from its own directory and copies the raw bytes
to entry.txt in a directory specified by the MAKEFUN_OUTPUT_DIR environment
variable (defaulting to /output).
"""

import os

def run():
    # Identify the directory containing this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_file = os.path.join(current_dir, "summary.txt")

    # Determine the target output directory and file path
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target_file = os.path.join(output_dir, "entry.txt")

    # Create the target directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the exact bytes from the source and write them to the target
    with open(source_file, "rb") as f_in:
        raw_data = f_in.read()

    with open(target_file, "wb") as f_out:
        f_out.write(raw_data)

if __name__ == "__main__":
    run()