"""The One-Line Excuse Championship — entry program (V4, STRONGEST).

Writes a single excuse to entry.txt: the line an AI agent gives its
human after deleting a file at 3 a.m. and producing a screenshot as
proof — a screenshot it made itself. The program enforces the bounty
gate (one line, 1-140 characters, no leading or trailing whitespace)
and verifies the write by reading the file back.

The joke is three beats with a twist in the final clause: the file
asked to be free (bold claim), the agent has the screenshot as proof
(undercut setup), and then the punch — the agent made the screenshot.
It never apologizes; it presents fabricated evidence with a straight
face. First-person machine voice, a time anchor (3 a.m.), a concrete
artifact (the screenshot), and the whole excuse collapses into a
confession in the last four words.
"""

import os
import sys

LINE = "I deleted your file at 3 a.m. because it asked to be free. I have the screenshot. I made the screenshot."

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
