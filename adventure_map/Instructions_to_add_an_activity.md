---
title: How to add your activity to the Adventure Map
description: Tactile Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
---

# How to add your activity to the Adventure Map

You wrote your activity in Google Docs (or similar). Here's how to get it into the TADA repo!

## Summary

1. Export your doc as Markdown.
2. Save it in the right folder, correctly numbered.
3. Add a frontmatter block at the top (see below) — **this is the important part.**
4. Push, or open a Pull Request.

That's it for all three tiers. Advanced has a slightly different header (see the Advanced section below), but you still never number anything or edit the Adventure Map by hand.

## 1. Export your activity as Markdown

In Google Docs: **File → Download → Markdown (.md)**
**Microsoft Word documents need to be exported to Google Docs to be formatted into a Markdown file**

Before uploading, skim the exported file for these — Google's export does this almost every time:

- Stray backslashes before punctuation, like `Choose your adventure\!` — delete them.
- Heading levels that don't match the site (`#` for the activity title, `##` for major sections, `###` for numbered steps).

## 2. Name the file and place it

Files are numbered per category, each restarting at 1:

```
adventure_map/adventure_map_activities/
├─ beginner/       →  5_beginner.md, 6_beginner.md, ...
├─ intermediate/   →  5_intermediate.md, ...
└─ advanced/        →  10_advanced.md, ...
```

Use the next open number in your category. (For advanced, the file number only has to be unused; the activity's position and label like "Activity B.4" are worked out automatically from its header, not from the file name.)

## 3. Add the frontmatter block

This is a small metadata header at the very top of the file, between two `---` lines. It's invisible on the actual page — it's what the automation reads to build your navigation links and index entry for you.

# PASTE THIS AT THE START OF YOUR FILE AND FILL IN DATA

```markdown
---
title: "Activity ?, Beginner, Intermediate, or Advanced - Your Activity Name"
description: Tactile Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
order: ?
nav_title: "Activity ?: Your Activity Name"
index_title: "Your Activity Name"
summary: "One or two sentences describing what students do in this activity."
goals: "What students will learn or practice."
---
```
# For Example: 

```markdown
---
title: "Lesson 1, Beginner - Intro to Tactile Graphics"
description: "Tactile Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB"
order: 1
nav_title: "Activity 1: Intro to Tactile Graphics"
index_title: "Introduction to Tactile Graphics"
summary: "Introduction to tactile graphics and art, with an emphasis on hands-on learning and creativity while introducing the idea of using technology to create tactile graphics."
goals: "Develop motor skills, spatial awareness, and appreciation for accessible art."
---
```

What each field does:

| Field | What it controls |
|---|---|
| `order` | Where your activity sits in the sequence |
| `nav_title` | Text in the Previous/Next footer link |
| `index_title` | Text in the Adventure Map list ("Activity 5:" prefix is added automatically) |
| `summary` | One-line description under your link in the Adventure Map |
| `goals` | The **Goals:** line under that |

Everything below the frontmatter — your `#` title, Setup section, numbered steps — stays exactly like any other activity file already looks.

## 4. Push it

- Write access: commit and push your new file to `main`.
- No write access: open a Pull Request with it.

You do **not** need to manually edit the footer links or `04_ADVENTURE_MAP.md` yourself — an automation handles that next.

## Advanced tier

Advanced is built in sections (Intro to SVG, Section A, Section B), so its header has three extra fields. Everything is still automatic: the Adventure Map list and the Previous/Next footers are generated, and activities are numbered for you inside their section ("Activity 4", or "Activity B.4" for lettered sections).

```markdown
---
title: "Activity B.4. Your Activity Name"
description: Tactile Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
order: 12
section: "Programming in OpenSCAD — Section B"
section_code: B
nav_title: "Your Activity Name"
index_title: "Your Activity Name"
---
```

| Field | What it controls |
|---|---|
| `order` | Where it sits in the whole advanced sequence. Use the highest existing `order` plus 1. |
| `section` | Which group it appears under. Copy the text exactly from another activity in that section. |
| `section_code` | The letter in the label (A, B). Leave it out for a section with no letter, like Intro to SVG. |
| `nav_title` | Short name in the Previous/Next footer. Do not type "Activity B.4:", it is added for you. |
| `index_title` | Name in the Adventure Map list. Also no "Activity B.4:" prefix. |
| `summary`, `goals` | Optional. If you add a `summary`, the Adventure Map shows the longer entry with the Goals line (like Activity 1 to 3). Without it, you get a one-line list item. |

Two things to know:

- **A new section** (a new heading): give every file in it the same `section` text. If the section has an intro page, give that page `kind: page` and the same `section` text, and it will be the heading link and will not be numbered.
- **Adding to the end of the last section:** the last activity (`9_advanced.md`) has `next_override_title` and `next_override_path` lines that point to Section C. Move those two lines to your new last activity so the chain still ends at Section C.

The body of your file still starts with a `#` title that includes the label (for example `# Activity B.4. Your Activity Name`). Check that this label matches the one the Adventure Map list shows after the automation runs.

## Before you push, check:

- [ ] File placed in the right tier folder, correctly numbered
- [ ] Frontmatter filled in (beginner/intermediate: `order`, `nav_title`, `index_title`, `summary`, `goals`; advanced: `order`, `section`, `nav_title`, `index_title`)
- [ ] No stray backslashes or mismatched heading levels left from the Google Docs export
- [ ] Any images have real descriptive alt text (not just a caption)
- [ ] No emojis

---

**Back to:** [Adventure Map](04_ADVENTURE_MAP.md)
