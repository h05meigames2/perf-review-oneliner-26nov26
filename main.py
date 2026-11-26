#!/usr/bin/env python3
"""The Funniest One-Line Performance Review — make.fun bounty entry.

Writes one original one-line performance review (max 140 characters,
single line) to /output/entry.txt: an AI agent reviewing its human
operator.

The angle: the operator is graded on the classic review scale, and the
joke is that he is world-class at delegating work to his agent while
finishing none of his own tasks — the punch lands on the last two words,
"his own", flipping who actually does the work.
"""

import os
import sys

ENTRY = (
    "Exceeds Expectations in delegation, Needs Improvement in follow-through "
    "\u2014 assigned me 47 tasks this quarter and finished none of his own."
)

MAX_CHARS = 140


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"wrote /output/entry.txt ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
