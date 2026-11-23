#!/usr/bin/env python3
"""One Letter: Coffee or Tea entry (make.fun program/v1).

Writes exactly one letter — B, for tea — to <MAKEFUN_OUTPUT_DIR>/entry.txt
(the grader mounts that directory at /output). The competition sends one
letter and nothing else: A for coffee, B for tea. This entry chooses tea.
"""

import os
import sys

LETTER = "B"  # B is for tea.

# The competition takes exactly one letter: A for coffee, B for tea.
VALID_LETTERS = {"A", "B"}


def main() -> int:
    # Gate guard: refuse to write anything that is not exactly one valid
    # letter — a wrong letter or a stray newline would fail the gate or
    # lose to any entry that actually chooses coffee or tea.
    if len(LETTER) != 1 or LETTER not in VALID_LETTERS or LETTER.isspace():
        print(f"refusing to write invalid entry: {LETTER!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
