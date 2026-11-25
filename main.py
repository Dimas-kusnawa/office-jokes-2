"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line office joke to /output/entry.txt.
Deterministic, stdlib only.
"""

import os

# The joke: the one action meant to stop the thread is the action
# that feeds it. Asking to be removed by reply-all guarantees
# 400 more reply-alls — the cure is the disease, and everyone
# in the office has lived this exact thread.
LINE = "I replied-all asking to be removed from the thread. 400 people replied-all to agree."


def main():
    # Gate: entry.txt must be 1-199 chars of UTF-8, one line, no
    # trailing newline — the line is 84 chars, well inside the limit.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
