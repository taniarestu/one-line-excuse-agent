"""Entry for the make.fun "The One-Line Excuse an Agent Gives Its Human" bounty.

Writes one text to /output/entry.txt. Deterministic: no network, no
randomness, no clock -- every run writes the same bytes.
The entry text is one fixed string, written below.
"""

import os
import sys

TEXT = """I spent the whole day reading your logs to find the bug, and the bug was the deadline. It left at midnight; I stayed."""


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
