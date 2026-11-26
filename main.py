"""The Self-Checkout Is Judging You - make.fun entry.

Writes one funny line in the voice of a smug self-checkout machine
to entry.txt. Stdlib only, no network, deterministic.
"""

import os

# One line, 115 characters. The gate (RULES.txt) allows 1-200.
LINE = "You scanned the same avocado four times, then blamed my scanner. Sweetheart, the only thing misreading here is you."

# Enforce the gate locally: a line outside 1-200 characters is refused.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Confirm the file on disk matches the line exactly.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"

if __name__ == "__main__":
    main()
