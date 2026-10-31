#!/usr/bin/env python3
"""Convert inline Pages CMS parent details into linked gecko lineage records."""
from pathlib import Path
import re
import unicodedata
import yaml

ROOT = Path("_geckos")


def slug(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_name = normalized.encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name).strip("-")


def read_record(path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        return None
    _, front, body = raw.split("---", 2)
    return yaml.safe_load(front) or {}, body


def write_record(path, data, body):
    front = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100)
    path.write_text("---\n" + front + "---" + body, encoding="utf-8")


def main():
    records = {}
    for path in ROOT.glob("*.md"):
        parsed = read_record(path)
        if parsed:
            data, _ = parsed
            name = str(data.get("name") or "").strip()
            if name:
                records.setdefault(name.casefold(), path)

    for path in list(ROOT.glob("*.md")):
        parsed = read_record(path)
        if not parsed:
            continue
        data, body = parsed
        changed = False
        for role, field, sex in (("new_sire", "sire", "Male"), ("new_dam", "dam", "Female")):
            inline = data.get(role)
            if not isinstance(inline, dict) or not str(inline.get("name") or "").strip():
                continue
            name = str(inline["name"]).strip()
            existing = records.get(name.casefold())
            if existing is None:
                stem = slug(name)
                if not stem:
                    raise ValueError("Parent name needs at least one Latin letter or digit")
                target = ROOT / (stem + ".md")
                index = 2
                while target.exists():
                    target = ROOT / f"{stem}-{index}.md"
                    index += 1
                parent = {
                    "animal_id": target.stem,
                    "name": name,
                    "status": "lineage",
                    "sex": sex,
                }
                for key in ("morph", "source", "parents"):
                    if inline.get(key):
                        parent[key] = inline[key]
                if inline.get("photo"):
                    parent["photos"] = [inline["photo"]]
                write_record(target, parent, "\n")
                records[name.casefold()] = target
            else:
                existing_data, _ = read_record(existing)
                if existing_data.get("sex") and existing_data["sex"].casefold() != sex.casefold():
                    raise ValueError(f"Existing parent {name!r} has conflicting sex; review before linking")
            data[field] = name
            del data[role]
            changed = True
        if changed:
            write_record(path, data, body)


if __name__ == "__main__":
    main()
