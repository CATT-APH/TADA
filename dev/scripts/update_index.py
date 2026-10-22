#!/usr/bin/env python3
"""
Regenerates the beginner/intermediate activity lists inside
04_ADVENTURE_MAP.md from each file's frontmatter (order, index_title,
summary, goals).

The advanced tier is generated too, but grouped: each file's `section:`
field becomes a heading, activities are auto-numbered inside their section
("Activity 1", or "Activity A.1" when `section_code: A` is set), and a file
with `kind: page` is the section's intro page (the heading links to it and
it is not numbered). Section C (the external STEM models guide) sits outside
the markers and is still hand-written.

Only rewrites the text between these marker pairs — everything else in
04_ADVENTURE_MAP.md, including "Coming Soon" placeholder lines placed
outside the markers, is left untouched:

    <!-- AUTO-GENERATED:beginner -->
    ...
    <!-- END AUTO-GENERATED:beginner -->

    <!-- AUTO-GENERATED:intermediate -->
    ...
    <!-- END AUTO-GENERATED:intermediate -->

    <!-- AUTO-GENERATED:advanced -->
    ...
    <!-- END AUTO-GENERATED:advanced -->

If the markers aren't present in the file yet, this script does nothing
for that tier (opt-in, non-destructive).
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import fm  # noqa: E402

ACTIVITIES_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "adventure_map", "adventure_map_activities")
MAP_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "adventure_map", "04_ADVENTURE_MAP.md")
AUTO_TIERS = ["beginner", "intermediate"]  # flat numbered lists; advanced is built by render_advanced()


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


def collect_advanced():
    items = []
    for path in sorted(glob.glob(os.path.join(ACTIVITIES_ROOT, "advanced", "*.md"))):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        order = fm.get_order(text)
        if order is None:
            continue
        data, _, _ = fm.parse(text)
        items.append({
            "order": order,
            "data": data,
            "relpath": f"adventure_map_activities/advanced/{os.path.basename(path)}",
        })
    items.sort(key=lambda i: i["order"])
    return items


def render_advanced(items):
    labels = fm.assign_labels(items)
    groups = {}
    for it in items:
        section = it["data"].get("section")
        if not section:
            print(f"WARNING: advanced file {it['relpath']} has no `section:`; left out of the index.")
            continue
        g = groups.setdefault(section, {"first": it["order"], "page": None, "acts": []})
        if it["data"].get("kind") == "page":
            g["page"] = it
        else:
            g["acts"].append(it)

    chunks = []  # list of (kind, text) so consecutive bullets stay tight
    for section, g in sorted(groups.items(), key=lambda kv: kv[1]["first"]):
        chunks.append(("h", f"### [{section}]({g['page']['relpath']})" if g["page"] else f"### {section}"))
        for it in g["acts"]:
            d = it["data"]
            title = d.get("index_title", d.get("title", ""))
            label = labels[id(it)]
            if d.get("summary", "").strip():
                entry = f"### [{label}: {title}]({it['relpath']})\n{d['summary'].strip()}"
                if d.get("goals", "").strip():
                    entry += f"\n\n**Goals:** {d['goals'].strip()}"
                chunks.append(("e", entry))
            else:
                chunks.append(("b", f"- [{label}: {title}]({it['relpath']})"))

    out = ""
    prev = None
    for kind, text in chunks:
        if prev is not None:
            out += "\n" if (prev == "b" and kind == "b") else "\n\n"
        out += text
        prev = kind
    return out + ("\n" if out else "")


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

    text, did = replace_marker_block(text, "advanced", render_advanced(collect_advanced()))
    if did:
        touched_tiers.append("advanced")

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
