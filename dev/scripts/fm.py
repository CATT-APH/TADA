"""
Minimal YAML-frontmatter helper. No PyYAML dependency on purpose — the
frontmatter in this repo is always flat "key: value" pairs, so a tiny
hand-rolled parser is safer than pulling in a library that might get
clever with unrelated syntax.

Only touches files that already have a `---`-delimited frontmatter
block AND (for the nav/index scripts) an `order:` field. Files without
`order:` are left completely alone, so adopting this is opt-in per file.
"""
import re

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse(text):
    """Return (dict, body_after_frontmatter, has_frontmatter: bool)."""
    m = FM_RE.match(text)
    if not m:
        return {}, text, False
    raw, body = m.group(1), text[m.end():]
    data = {}
    for line in raw.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith('"') and val.endswith('"') and len(val) >= 2:
            val = val[1:-1]
        data[key] = val
    return data, body, True


def get_order(text):
    data, _, _ = parse(text)
    if "order" not in data:
        return None
    try:
        return int(data["order"])
    except ValueError:
        return None


def get(text, key, default=None):
    data, _, _ = parse(text)
    return data.get(key, default)


def assign_labels(items):
    """Auto-number activities that opt in with a `section:` field.

    items: list of dicts with keys "order" (int) and "data" (frontmatter dict),
    already sorted by order. Returns {id(item): "Activity 3"} or
    {id(item): "Activity A.2"} - the number is the item's position inside its
    section (counting only kind != page), so authors never type a number.

    `section_code: A` makes the label "Activity A.<n>"; without a code it is
    "Activity <n>". Items with kind: page (section intro pages) get no label.
    Items with no `section:` (beginner / intermediate) are skipped.
    """
    counts = {}
    labels = {}
    for it in items:
        data = it["data"]
        section = data.get("section")
        if not section or data.get("kind") == "page":
            continue
        counts[section] = counts.get(section, 0) + 1
        n = counts[section]
        code = data.get("section_code", "").strip()
        labels[id(it)] = f"Activity {code}.{n}" if code else f"Activity {n}"
    return labels
