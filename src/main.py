# src/main.py
"""
Minimal demo script for Task B.
- Purpose: generate a small CSV so we can run, get outputs, and analyze.
- Outputs:
    - outputs/results.csv  : 10 demo rows
    - stdout               : confirmation message
"""

import csv, random, pathlib

def generate_rows(n=10):
    """Return n rows of demo data as (step, score)."""
    return [(i, round(random.random(), 4)) for i in range(n)]

def write_csv(path):
    """Write rows to CSV at 'path' and return the path."""
    rows = generate_rows(10)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["step", "score"])
        w.writerows(rows)
    return path

if __name__ == "__main__":
    out_dir = pathlib.Path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "results.csv"
    write_csv(out_path)
    print(f"Wrote {out_path}")
