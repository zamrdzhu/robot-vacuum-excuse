"""The robot vacuum's best excuse (140 characters or fewer).

Prints the excuse to stdout and writes the exact same excuse, with
no trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the excuse is a constant in this file.

The gate for this bounty is 1 to 140 characters of UTF-8 text, so the
program refuses to write anything outside that range.
"""

import os
import sys

LINE = (
    "I did not miss that spot. My sensors found a crumb with "
    "diplomatic immunity, and I respectfully declined to engage."
)


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
