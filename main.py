#!/usr/bin/env python3
"""One-Liner Laugh Lab — entry program.

Writes one line to /output/entry.txt: the robot vacuum's courtroom
defence after eating a sock — the sock was disguised as a dust
bunny, it was framed, and it has the lint to prove it. One line of
UTF-8 text inside the gate of 1 to 200 characters, no trailing
newline.
"""

import os
from pathlib import Path

DEFENCE = (
    "Your honour, the sock was disguised as a dust bunny. I was "
    "framed, and I have the lint to prove it."
)


def produce_entry() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    # No trailing newline: the defence stands alone at 99 characters.
    entry.write_text(DEFENCE, encoding="utf-8")


if __name__ == "__main__":
    produce_entry()
