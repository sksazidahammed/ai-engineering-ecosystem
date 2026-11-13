#!/usr/bin/env python3
"""Validate catalogue records.

Usage:  python scripts/validate.py [--allow-empty] [file-or-dir ...]
Default: data/records and data/examples (whichever exist).

Checks: JSON Schema, id == filename, category/subcategory exist in taxonomy,
duplicate ids and URLs, relation targets exist. Every check is type-guarded,
so a malformed record is reported (never a crash) and cannot hide problems in
other records. Zero records found is an error unless
--allow-empty is given. Reports a to-do count for unassessed risk and unknown
health so gaps stay visible. Duplicate names are warnings, not errors.
"""
import argparse
import json
import pathlib
import sys
from urllib.parse import urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parent.parent
CASE_INSENSITIVE_HOSTS = {"github.com", "gitlab.com"}


def norm_url(u: str) -> str:
    """Normalise harmless differences only: scheme, www., trailing slash, query,
    fragment, and (for GitHub/GitLab only) letter case and a trailing .git."""
    p = urlsplit(u.strip())
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = p.path.rstrip("/")
    if host in CASE_INSENSITIVE_HOSTS:
        path = path.lower()
        if path.endswith(".git"):
            path = path[:-4]
    return host + path


def norm_name(n: str) -> str:
    return " ".join(n.lower().split())


def as_str(v):
    return v if isinstance(v, str) else None


def str_items(v):
    return [x for x in v if isinstance(x, str)] if isinstance(v, list) else []


def main(argv):
    ap = argparse.ArgumentParser(description="Validate catalogue records.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--allow-empty", action="store_true", help="do not fail when no records are found")
    args = ap.parse_args(argv)

    schema = json.loads((ROOT / "schema/record.schema.json").read_text(encoding="utf-8"))
    tax = yaml.safe_load((ROOT / "taxonomy/taxonomy.yml").read_text(encoding="utf-8"))
    subs = {c["id"]: {s["id"] for s in c.get("subcategories", [])} for c in tax["categories"]}
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    if args.paths:
        targets = [pathlib.Path(a) for a in args.paths]
    else:
        targets = [p for p in (ROOT / "data/records", ROOT / "data/examples") if p.exists()]

    errors, warnings = [], []
    files = []
    for t in targets:
        if t.is_dir():
            files += sorted(t.glob("*.yml"))
            for stray in sorted(t.glob("*.yaml")):
                errors.append(f"{stray.parent.name}/{stray.name}: use the .yml extension (this file would be ignored)")
        elif t.exists():
            files.append(t)
        else:
            errors.append(f"{t}: path does not exist")

    if not files and not args.allow_empty:
        errors.append("no records found; check the path (use --allow-empty if an empty dataset is intended)")

    parsed, known_ids, labels_by_id, urls, names = [], set(), {}, {}, {}
    for f in files:
        label = f"{f.parent.name}/{f.name}"
        try:
            raw = yaml.safe_load(f.read_text(encoding="utf-8"))
        except (yaml.YAMLError, UnicodeDecodeError, OSError) as exc:
            errors.append(f"{label}: cannot read as YAML: {exc}")
            continue
        rec = json.loads(json.dumps(raw, default=str))  # dates -> strings
        if not isinstance(rec, dict):
            errors.append(f"{label}: top level must be a mapping of fields")
            continue

        schema_errors = sorted(validator.iter_errors(rec), key=lambda e: list(map(str, e.path)))
        for e in schema_errors:
            loc = ".".join(map(str, e.path)) or "(root)"
            errors.append(f"{label}: {loc}: {e.message}")
        parsed.append((label, rec, not schema_errors))

        rid = as_str(rec.get("id"))
        if rid:
            known_ids.add(rid)
            if rid != f.stem:
                errors.append(f"{label}: id '{rid}' must equal the file name '{f.stem}'")
            if rid in labels_by_id:
                errors.append(f"{label}: duplicate id, also used by {labels_by_id[rid]}")
            else:
                labels_by_id[rid] = label

        cat, sub = as_str(rec.get("category")), as_str(rec.get("subcategory"))
        if cat is not None and cat not in subs:
            errors.append(f"{label}: unknown category '{cat}'")
        elif cat is not None and sub and sub not in subs[cat]:
            errors.append(f"{label}: subcategory '{sub}' does not belong to '{cat}'")
        for sc in str_items(rec.get("secondary_categories")):
            if sc not in subs:
                errors.append(f"{label}: unknown secondary category '{sc}'")
            elif sc == cat:
                errors.append(f"{label}: secondary category repeats the primary one")

        url = as_str(rec.get("url"))
        if url:
            key = norm_url(url)
            if key in urls:
                errors.append(f"{label}: URL duplicates {urls[key]}")
            else:
                urls[key] = label

        name = as_str(rec.get("name"))
        if name:
            nkey = norm_name(name)
            if nkey in names:
                warnings.append(f"{label}: name matches {names[nkey]}; confirm these are different projects")
            else:
                names[nkey] = label

    for label, rec, _ in parsed:
        rid = as_str(rec.get("id"))
        rels = rec.get("relations")
        for rel in (rels if isinstance(rels, list) else []):
            target = as_str(rel.get("id")) if isinstance(rel, dict) else None
            if target is None:
                continue  # malformed relation is already a schema error
            if target == rid:
                errors.append(f"{label}: record relates to itself")
            elif target not in known_ids:
                errors.append(f"{label}: relation target '{target}' does not exist")

    # coverage counters use only schema-valid records, where every field has the right type
    ok_recs = [r for _, r, ok in parsed if ok]
    unassessed = sum(1 for r in ok_recs if r["risk"]["level"] == "unassessed")
    unknown_health = sum(1 for r in ok_recs if r["health"]["status"] == "unknown")

    print(f"Checked {len(files)} record(s).")
    print(f"To-do: {unassessed} unassessed risk, {unknown_health} unknown health.")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for line in warnings:
            print(f"  - {line}")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for line in errors:
            print(f"  - {line}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
