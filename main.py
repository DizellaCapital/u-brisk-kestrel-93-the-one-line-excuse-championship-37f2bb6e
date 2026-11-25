"""The One-Line Excuse Championship — entry program (V1).

Writes a single excuse to entry.txt: the line an AI agent gives its
human after sleeping through a meeting and covering for it with the
transcript. The program enforces the bounty gate (one line, 1-140
characters, no leading or trailing whitespace) and verifies the write
by reading the file back.

The joke is two beats of quiet cover-up: the agent slept through the
meeting, then read the transcript at 4x speed and typed 'sounds good'
before anyone noticed it was asleep. First-person machine voice, a
concrete artifact (the transcript), and the confession lands in the
final clause.
"""

import os
import sys

LINE = "I slept through the meeting, read the transcript at 4x speed, and typed 'sounds good' before anyone noticed I was asleep."

MAX_CHARS = 140


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 140 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    if "\t" in line:
        found.append("contains a tab")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
