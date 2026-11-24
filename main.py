#!/usr/bin/env python3
"""Write one short out-of-office text for a make.fun bounty.

The text is written as UTF-8 bytes with no trailing newline to
entry.txt inside the output folder.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
