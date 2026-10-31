#!/usr/bin/env python3
"""Ensure YAML gecko hatch dates are strings for Pages CMS."""
from pathlib import Path
import re

ROOT = Path("_geckos")
DATE = re.compile(r"^(hatch_date:\\s*)([0-9]{1,4})(\\s*(?:#.*)?)$", re.MULTILINE)


def normalize():
    changed = []
    for path in sorted(ROOT.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        if not raw.startswith("---\n"):
            continue
        end = raw.find("\n---", 4)
        if end < 0:
            continue
        front, rest = raw[:end], raw[end:]
        fixed = DATE.sub(lambda m: m.group(1) + "'" + m.group(2) + "'" + m.group(3), front)
        if fixed != front:
            path.write_text(fixed + rest, encoding="utf-8")
            changed.append(str(path))
    print("Normalized hatch dates:", ", ".join(changed) if changed else "none")


if __name__ == "__main__":
    normalize()
