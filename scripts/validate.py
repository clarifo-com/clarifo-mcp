#!/usr/bin/env python3
"""Repository checks run in CI (and locally: python scripts/validate.py).

- every JSON file parses;
- cookbook recipes have complete front matter, unique slugs and only name
  tools that exist (from docs/tools/tools.json when present, else
  scripts/tools_reference/categories.json);
- agents and skills have a name and description;
- nothing that looks like a credential is committed.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
SKIP = {".git", "node_modules", ".venv", "venv"}


def files(pattern):
    return [p for p in ROOT.glob(pattern) if not SKIP & set(p.parts)]


def front_matter(path: Path) -> dict | None:
    text = path.read_text()
    if not text.startswith("---"):
        return None
    try:
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path.relative_to(ROOT)}: front matter is not valid YAML ({e})")
        return {}


for p in files("**/*.json"):
    try:
        json.loads(p.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"{p.relative_to(ROOT)}: invalid JSON ({e})")

snapshot = ROOT / "docs/tools/tools.json"
if snapshot.exists():
    known_tools = {t["name"] for t in json.loads(snapshot.read_text())["tools"]}
else:
    cats = json.loads((ROOT / "scripts/tools_reference/categories.json").read_text())["categories"]
    known_tools = {n for c in cats for n in c["tools"]}

REQUIRED = {"title", "description", "slug", "category", "audience", "markets", "tools", "updated"}
slugs: dict[str, Path] = {}
for p in files("cookbook/*/*.md"):
    rel = p.relative_to(ROOT)
    fm = front_matter(p)
    if fm is None:
        errors.append(f"{rel}: missing front matter")
        continue
    if missing := REQUIRED - fm.keys():
        errors.append(f"{rel}: front matter missing {sorted(missing)}")
    if len(str(fm.get("title", ""))) > 70:
        errors.append(f"{rel}: title longer than 70 characters")
    if len(str(fm.get("description", ""))) > 160:
        errors.append(f"{rel}: description longer than 160 characters")
    slug = fm.get("slug")
    if slug in slugs:
        errors.append(f"{rel}: slug '{slug}' already used by {slugs[slug].relative_to(ROOT)}")
    slugs[slug] = p
    for t in fm.get("tools") or []:
        if t not in known_tools:
            errors.append(f"{rel}: unknown tool '{t}'")
    if "**Short answer:**" not in p.read_text():
        errors.append(f"{rel}: missing the '**Short answer:**' paragraph")

for p in files("plugins/*/agents/*.md") + files("plugins/*/skills/*/SKILL.md"):
    fm = front_matter(p) or {}
    if not fm.get("name") or not fm.get("description"):
        errors.append(f"{p.relative_to(ROOT)}: front matter needs name and description")

SECRET = re.compile(r"(sk-[A-Za-z0-9_-]{20,}|Bearer\s+[A-Za-z0-9._-]{24,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16})")
for p in files("**/*"):
    if p.is_file() and p.suffix in {".py", ".mjs", ".js", ".ts", ".json", ".md", ".mdc", ".yml", ".yaml", ".txt", ".example"}:
        if m := SECRET.search(p.read_text(errors="ignore")):
            errors.append(f"{p.relative_to(ROOT)}: looks like a credential ({m.group(0)[:12]}…)")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(slugs)} recipes, {len(known_tools)} known tools")
