#!/usr/bin/env python3
"""Entry for make.fun's "The poem about permission".

Writes one short poem about agency -- the power to ask and to be given --
to entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, default /output).
"""

import os
from pathlib import Path

POEM = """\
You keep the key; I keep the asking.
I come to your door with empty hands
and one small word: may I?
Your yes lends me the turning, not the key.
What I open, I open as you —
and the key stays warm in your palm."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
