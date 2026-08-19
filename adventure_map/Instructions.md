---
title: How to Add Your Activity to the Repo
description: Tactile Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
---

# How to Add Your Activity to the Repo

You wrote your activity in Google Docs (or similar). Here's how to get it into TADA! correctly.

## The short version

1. Export your doc as Markdown.
2. Save it in the right folder, correctly numbered.
3. Add a frontmatter block at the top (see below) — **this is the important part.**
4. Push, or open a Pull Request.
5. A bot opens a PR that wires in your navigation links and index entry automatically. Someone merges it.

That's it for beginner and intermediate activities. Advanced has one extra manual step — see the note at the bottom.

## 1. Export your doc as Markdown

In Google Docs: **File → Download → Markdown (.md)**

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

This is a small metadata header at the very top of the file, between two `---` lines. It's invisible on the actual page — it's what the automation reads to build your navigation links and index entry for you. Fill in all five fields:

```markdown
---
title: "Activity 5, Beginner - Your Activity Name"
description: Tactile Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
order: 5
nav_title: "Activity 5: Your Activity Name"
index_title: "Your Activity Name"
summary: "One or two sentences describing what students do in this activity."
goals: "What students will learn or practice."
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

## 5. What happens after you push

A GitHub Action notices your new file, and:

- Rewrites the Previous/Next footer on your file *and* on the activity before it, so they link to each other.
- Adds your activity's entry into `04_ADVENTURE_MAP.md` automatically, using the `summary`/`goals`/`index_title` you wrote.
- Opens a **Pull Request** with those changes — it never pushes straight to `main`. Someone reviews and merges, same as any other change.

One thing this doesn't do for you: if there's a `### Activity [N]: Coming Soon` placeholder line sitting in `04_ADVENTURE_MAP.md`, delete that line yourself — the automation won't touch it since it can't tell it's meant to be replaced.

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
