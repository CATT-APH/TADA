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

That's it for beginner and intermediate activities. Advanced has one extra manual step (see the note at the bottom).

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

Use the next open number in your category.

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

## Advanced tier: one extra manual step

Advanced activities get their footer links automated the same way. But the Advanced section of `04_ADVENTURE_MAP.md` mixes real activities with hand-written section headers (like "Section A: Making 2D Shapes in OpenSCAD") that don't correspond to any file — so that index section is never auto-generated. If you're adding an advanced activity, add its line to `04_ADVENTURE_MAP.md` yourself, in the same format as the ones already there.

## Before you push, check:

- [ ] File placed in the right tier folder, correctly numbered
- [ ] Frontmatter has `order`, `nav_title`, `index_title`, `summary`, and `goals` filled in
- [ ] No stray backslashes or mismatched heading levels left from the Google Docs export
- [ ] Any images have real descriptive alt text (not just a caption)
- [ ] No emojis

---

**Back to:** [Adventure Map](04_ADVENTURE_MAP.md)
