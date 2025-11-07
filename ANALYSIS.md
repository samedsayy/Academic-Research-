**Purpose:** Generate a simple CSV to demonstrate execution, outputs, and analysis.

**Outputs:** `outputs/results.csv` and `outputs/run-log.txt`.

**What the code does (brief):**
- Creates 10 random (step, score) rows.
- Writes them to CSV.
- Prints a confirmation line.

**Limitations:**
- No input parameters via CLI.
- No tests/CI or dependency pins.
- Hard-coded output path.

**Possible improvements/extensions:**
- Add CLI args (e.g., --rows, --out).
- Add unit tests and GitHub Actions CI.
- Add logging and type hints.
- Package with `pyproject.toml`; pin deps.
