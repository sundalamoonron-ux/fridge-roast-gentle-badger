#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh -- make.fun entry.

Writes one line (<= 200 characters) roasting a smart fridge to
<output>/entry.txt: a smart fridge with a touchscreen, a camera, and
opinions about my cheese -- but no ice.
"""

import os
import sys

# The line: a three-item list of smart features (touchscreen, camera,
# opinions about cheese) undercut by the punchline -- the one thing it
# doesn't have is ice. A roast of feature bloat vs core failure,
# specific to a "smart" fridge and tight at 103 characters.
LINE = "My smart fridge has a touchscreen, a camera, and opinions about my cheese. What it doesn't have is ice."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
