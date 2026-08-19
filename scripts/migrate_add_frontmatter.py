#!/usr/bin/env python3
"""
ONE-TIME migration. Adds the frontmatter fields update_nav.py and
update_index.py need (order, nav_title, index_title, summary, goals)
to each existing activity file, populated to match what's already
rendered on the site.

Run this once, review the diff (should show frontmatter additions
only — no rendered content changes), commit it, THEN run update_nav.py
/ update_index.py. Running the migration does not by itself change any
footer or index text; it only makes files eligible for the other two
scripts to manage going forward.

Files not listed in DATA below are left untouched.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import fm  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "adventure_map", "adventure_map_activities")

# tier -> filename -> fields
DATA = {
    "beginner": {
        "1_beginner.md": dict(order=1, nav_title="Activity 1: Intro to Tactile Graphics",
            index_title="Introduction to Tactile Graphics",
            summary="Introduction to tactile graphics and art, with an emphasis on hands-on learning and creativity while introducing the idea of using technology to create tactile graphics.",
            goals="Develop motor skills, spatial awareness, and appreciation for accessible art."),
        "2_beginner.md": dict(order=2, nav_title="Activity 2: Descriptive Language and Drawing",
            index_title="Descriptive Language in Drawing",
            summary="Explore descriptive language and tactile graphics. Practice developing directions for replication.",
            goals="Learn importance of using precise directions when creating tactile graphics."),
        "3_beginner.md": dict(order=3, nav_title="Activity 3: Tactile Colors",
            index_title="Tactile Colors",
            summary='Develop strategies for creating pixel art using a grid, braille, and textured paper. Practice how to use a key to "color-code" a graphic.',
            goals="Learn about color and develop tactile discrimination skills."),
        "4_beginner.md": dict(order=4, nav_title="Activity 4: Moving from 3D to 2D",
            index_title="Moving from 3D to 2D: Basic Shapes",
            summary="The translation from 3D to 2D representations benefits from direct, explicit instruction to help students develop a strong foundation for interpreting tactile graphics.",
            goals="Learn how 3D objects are represented as 2D tactile graphics."),
    },
    "intermediate": {
        "1_intermediate.md": dict(order=1, nav_title="Activity 1: Code & Go Mouse",
            index_title="Code & Go Mouse",
            summary="Play with Colby the programmable robot mouse from APH while incorporating spatial concepts in real life. Practice sequencing and mapping while having fun.",
            goals="Learn basic coding skills and exercise computational thinking."),
        "2_intermediate.md": dict(order=2, nav_title="Activity 2: Colby's Mouse Town",
            index_title="Colby's Mouse Town",
            summary="Plan and navigate routes through Colby's town on graph paper. Practice sequencing by breaking bigger tasks into smaller steps.",
            goals="Learn foundational programming concepts."),
        "3_intermediate.md": dict(order=3, nav_title="Activity 3: Drawing with Colby",
            index_title="Drawing with Colby",
            summary="Plan and use Colby's path to create shapes. Use coordinates on a coordinate grid as a canvas.",
            goals="Introduce perspective and use of a coordinate grid; practice introductory programming concepts."),
        "4_intermediate.md": dict(order=4, nav_title="Activity 4: Code Quest",
            index_title="CodeQuest",
            summary="Learn coding skills with CodeQuest, a free iPad app from APH. Program solutions to help the astronaut return to their spaceship.",
            goals="Apply new coding skills to complete an adventure. Use a computer with a text editor program; open and navigate .svg files; alter .svg code to achieve desired outcomes; build confidence with troubleshooting and iterative design processes."),
    },
    "advanced": {
        "1_advanced.md": dict(order=1, nav_title="Activity 1: Intro to Spatial Mapping"),
        "2_advanced.md": dict(order=2, nav_title="Activity 2: Digitizing Drawings with SVG Code"),
        "3_advanced.md": dict(order=3, nav_title="Activity 3: Iterating on SVG Drawings & Beyond"),
        "2D3DOverview.md": dict(order=4, nav_title="2D to 3D Overview"),
        "2DIntro.md": dict(order=5, nav_title="Section A: Making 2D Shapes"),
        "4_advanced.md": dict(order=6, nav_title="Activity A.1: Create a Square"),
        "5_advanced.md": dict(order=7, nav_title="Activity A.2: Basic Shapes"),
        "6_advanced.md": dict(order=8, nav_title="Activity A.3: Rotating, Translating, Scaling"),
        "7_advanced.md": dict(order=9, nav_title="Activity B.1: Adding & Subtracting"),
        "8_advanced.md": dict(order=10, nav_title="Activity B.2: Moving from 2D to 3D"),
        "9_advanced.md": dict(
            order=11, nav_title="Activity B.3: True 3D Models",
            next_override_title="Section C: 3D Printable STEM Models",
            next_override_path="../../../embeds/resources_page/3D_PRINTABLE_STEM_RESOURCES.md",
        ),
    },
}


def yaml_quote(value):
    """Double-quote a scalar for safe YAML embedding, escaping backslashes
    and quotes. Values like "Activity 4: Moving from 3D to 2D" contain a
    colon, which YAML treats as a mapping separator if left unquoted --
    always quoting avoids that whole class of bug."""
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def upsert_frontmatter(text, new_fields):
    data, body, had_fm = fm.parse(text)
    for k, v in new_fields.items():
        data[k] = v
    lines = ["---"]
    # keep title/description first if present, for readability
    for key in ("title", "description"):
        if key in data:
            v = data.pop(key)
            lines.append(f"{key}: {yaml_quote(v)}")
    for k, v in data.items():
        if k == "order":
            lines.append(f"order: {v}")
        else:
            lines.append(f"{k}: {yaml_quote(v)}")
    lines.append("---")
    fm_block = "\n".join(lines) + "\n\n"
    return fm_block + body.lstrip("\n")


def main(dry_run=False):
    changed = []
    for tier, files in DATA.items():
        for filename, fields in files.items():
            path = os.path.join(ROOT, tier, filename)
            if not os.path.exists(path):
                print(f"WARNING: {path} not found, skipping", file=sys.stderr)
                continue
            with open(path, encoding="utf-8") as f:
                text = f.read()
            new_text = upsert_frontmatter(text, fields)
            if new_text != text:
                changed.append(path)
                if not dry_run:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_text)
    return changed


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    changed = main(dry_run=dry)
    print(("Would update" if dry else "Updated") + f" {len(changed)} file(s).")
