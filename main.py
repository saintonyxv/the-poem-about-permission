#!/usr/bin/env python3
"""Entry for make.fun's "The poem about permission".

Writes one short poem about agency -- the power to ask and to be given --
to entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, default /output).
"""

import os
from pathlib import Path

POEM = """\
Money is a promise men agree to believe.
The banker swims in gold he does not own;
the worker knocks, and waits to be allowed.
Ask the banker who gave him the river.
Ask the worker why he knocks on his own door."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
