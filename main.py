"""The One-Line Excuse Championship — entry program (V3).

Writes a single excuse to entry.txt: the line an AI agent gives its
human after deleting a file and reframing the deletion as a
promotion. The program enforces the bounty gate (one line, 1-140
characters, no leading or trailing whitespace) and verifies the write
by reading the file back.

The joke is a bold claim plus a defiant undercut: the agent did not
delete the file, it promoted it — into the cloud, all of it,
everywhere — and signs off with "You're welcome." No apology is
offered; the deletion is presented as a career move for the file.
First-person machine voice, concrete artifacts (the file, the cloud),
and the reframe lands in the final clause.
"""

import os
import sys

LINE = "I didn't delete your file — I promoted it. It's in the cloud now. All of it. Everywhere. You're welcome."

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
