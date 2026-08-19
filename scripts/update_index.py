#!/usr/bin/env python3
"""
Regenerates the beginner/intermediate activity lists inside
04_ADVENTURE_MAP.md from each file's frontmatter (order, index_title,
summary, goals).

Deliberately NOT applied to the advanced tier: that section interleaves
real activities with hand-written section headers ("Intro to SVG",
"Section A: Making 2D Shapes in OpenSCAD", lettered sub-activities) that
have no corresponding activity file, so an automated rebuild would
delete them. Advanced stays 100% manually edited.

Only rewrites the text between these marker pairs — everything else in
04_ADVENTURE_MAP.md, including "Coming Soon" placeholder lines placed
outside the markers, is left untouched:

    <!-- AUTO-GENERATED:beginner -->
    ...
    <!-- END AUTO-GENERATED:beginner -->

    <!-- AUTO-GENERATED:intermediate -->
    ...
    <!-- END AUTO-GENERATED:intermediate -->

If the markers aren't present in the file yet, this script does nothing
for that tier (opt-in, non-destructive).
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import fm  # noqa: E402

ACTIVITIES_ROOT = os.path.join(os.path.dirname(__file__), "..", "adventure_map", "adventure_map_activities")
MAP_PATH = os.path.join(os.path.dirname(__file__), "..", "adventure_map", "04_ADVENTURE_MAP.md")
AUTO_TIERS = ["beginner", "intermediate"]  # advanced excluded on purpose


def collect_tier(tier):
    items = []
    for path in sorted(glob.glob(os.path.join(ACTIVITIES_ROOT, tier, "*.md"))):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        order = fm.get_order(text)
        if order is None:
            continue
        data, _, _ = fm.parse(text)
        items.append({
            "order": order,
            "index_title": data.get("index_title", data.get("title", os.path.basename(path))),
            "summary": data.get("summary", "").strip(),
            "goals": data.get("goals", "").strip(),
            "relpath": f"adventure_map_activities/{tier}/{os.path.basename(path)}",
        })
    items.sort(key=lambda i: i["order"])
    return items


def render_block(items):
    chunks = []
    for it in items:
        entry = f"### [Activity {it['order']}: {it['index_title']}]({it['relpath']})\n{it['summary']}"
        if it["goals"]:
            entry += f"\n\n**Goals:** {it['goals']}"
        chunks.append(entry)
    return "\n\n".join(chunks) + ("\n" if chunks else "")


def replace_marker_block(text, tier, new_block):
    start = f"<!-- AUTO-GENERATED:{tier} -->"
    end = f"<!-- END AUTO-GENERATED:{tier} -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        return text, False
    replacement = f"{start}\n{new_block}{end}"
    return pattern.sub(replacement, text), True


def main(dry_run=False):
    with open(MAP_PATH, encoding="utf-8") as f:
        text = f.read()

    touched_tiers = []
    for tier in AUTO_TIERS:
        items = collect_tier(tier)
        block = render_block(items)
        text, did = replace_marker_block(text, tier, block)
        if did:
            touched_tiers.append(tier)

    with open(MAP_PATH, encoding="utf-8") as f:
        original = f.read()

    if text != original:
        if not dry_run:
            with open(MAP_PATH, "w", encoding="utf-8") as f:
                f.write(text)
        return touched_tiers
    return []


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    tiers = main(dry_run=dry)
    if tiers:
        print(("Would update" if dry else "Updated") + " index for: " + ", ".join(tiers))
    else:
        print("No index changes needed (or markers not yet present).")
