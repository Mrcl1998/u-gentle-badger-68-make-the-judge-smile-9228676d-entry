#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

Pure standard library. Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = (
    'A stranger at the bus stop pressed his umbrella into my hands, '
    'said "you need it more," and walked off into the rain whistling '
    "\u2014 I stayed dry, holding his terrible tune."
)


def main():
    text = ENTRY
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
