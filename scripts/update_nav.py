#!/usr/bin/env python3
"""
Rewrites the Previous/Next footer on every activity file that has opted
in via an `order:` frontmatter field. Files without `order:` are left
untouched — nothing changes until you migrate a file.

Ordering is explicit (the `order` number), NOT derived from filenames,
so it works for the advanced tier where the real reading sequence
(1, 2, 3, 2D3DOverview, 2DIntro, 4, 5, ...) doesn't match filename order.

Optional per-file frontmatter overrides, for edges that don't point to
another activity file in the same folder:
    next_override_title: "Section C: Guide to Published 3D Printable STEM Models"
    next_override_path: "../../../embeds/resources_page/3D_PRINTABLE_STEM_RESOURCES.md"
    prev_override_title: "..."
    prev_override_path: "..."

Only ever rewrites the text after the LAST "---" divider in the file
(the existing footer). Everything above that — including the activity
content itself — is never touched.
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import fm  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "adventure_map", "adventure_map_activities")
TIERS = ["beginner", "intermediate", "advanced"]
DOWNLOAD_LINK = "[Download the whole thing](https://github.com/aabdurmohammed-source/TADA/archive/refs/heads/main.zip)"
BACK_LINK = "**Back to:** [Adventure Map](../../04_ADVENTURE_MAP.md)"

FOOTER_DIVIDER = "\n---\n\n"


def build_footer(prev, nxt):
    parts = []
    if prev:
        parts.append(f"**Previous:** [{prev[0]}]({prev[1]})")
    parts.append(DOWNLOAD_LINK)
    if nxt:
        parts.append(f"**Next:** [{nxt[0]}]({nxt[1]})")
    parts.append(BACK_LINK)
    return " · ".join(parts) + "\n"


def replace_footer(text, new_footer):
    idx = text.rfind(FOOTER_DIVIDER)
    if idx == -1:
        # No existing footer divider — append one rather than guessing.
        base = text.rstrip("\n")
        return base + "\n\n---\n\n" + new_footer
    return text[: idx + len(FOOTER_DIVIDER)] + new_footer


def main(dry_run=False):
    changed = []
    for tier in TIERS:
        folder = os.path.join(ROOT, tier)
        items = []
        for path in sorted(glob.glob(os.path.join(folder, "*.md"))):
            with open(path, encoding="utf-8") as f:
                text = f.read()
            order = fm.get_order(text)
            if order is None:
                continue  # opt-in only
            data, _, _ = fm.parse(text)
            nav_title = data.get("nav_title") or data.get("title") or os.path.basename(path)
            items.append({
                "path": path,
                "filename": os.path.basename(path),
                "order": order,
                "nav_title": nav_title,
                "data": data,
                "text": text,
            })
        items.sort(key=lambda i: i["order"])

        for i, item in enumerate(items):
            data = item["data"]

            if data.get("prev_override_title") and data.get("prev_override_path"):
                prev = (data["prev_override_title"], data["prev_override_path"])
            elif i > 0:
                prev = (items[i - 1]["nav_title"], items[i - 1]["filename"])
            else:
                prev = None

            if data.get("next_override_title") and data.get("next_override_path"):
                nxt = (data["next_override_title"], data["next_override_path"])
            elif i < len(items) - 1:
                nxt = (items[i + 1]["nav_title"], items[i + 1]["filename"])
            else:
                nxt = None

            new_footer = build_footer(prev, nxt)
            new_text = replace_footer(item["text"], new_footer)
            if new_text != item["text"]:
                changed.append(item["path"])
                if not dry_run:
                    with open(item["path"], "w", encoding="utf-8") as f:
                        f.write(new_text)

    return changed


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    changed = main(dry_run=dry)
    if changed:
        print(("Would update" if dry else "Updated") + f" {len(changed)} file(s):")
        for p in changed:
            print(" -", os.path.relpath(p))
    else:
        print("No footer changes needed.")
