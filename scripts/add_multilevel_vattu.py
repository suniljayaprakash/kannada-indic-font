#!/usr/bin/env python3
"""
Option A multi-level vattu implementation:
  1. Add 'bottom' and 'right' anchors to all 36 *vattu-kannada glyphs
  2. Create 36 *vattu_r-kannada glyphs (same paths, _right + right anchors)
  3. Add 'vatu' OpenType feature for contextual right-side vattu substitution
"""

import re

FONT_FILE = "Bilvafont-experiments.glyphs"

# Consonants in blwf order (matches blwf feature)
BLWF_ORDER = [
    "ka", "kha", "ga", "gha", "nga",
    "ca", "cha", "ja", "jha", "nya",
    "tta", "ttha", "dda", "ddha", "nna",
    "ta", "tha", "da", "dha", "na",
    "pa", "pha", "ba", "bha", "ma",
    "ya", "ra", "rra", "la", "va",
    "sha", "ssa", "sa", "ha", "lla", "llla",
]


def find_glyph_block(content, glyph_name):
    """Return (start, end) byte offsets of the top-level glyph dict for glyph_name."""
    needle = f'glyphname = "{glyph_name}";'
    name_idx = content.find(needle)
    if name_idx == -1:
        return None, None

    # Scan backward from the glyphname to find the { that opens this glyph block.
    # Between that { and glyphname there are only simple key=value lines (category,
    # direction) — no nested braces — so the first { we hit going backward is correct.
    pos = name_idx - 1
    while pos >= 0 and content[pos] != '{':
        pos -= 1
    block_start = pos

    # Count braces forward to find the matching }
    depth = 0
    pos = block_start
    while pos < len(content):
        if content[pos] == '{':
            depth += 1
        elif content[pos] == '}':
            depth -= 1
            if depth == 0:
                return block_start, pos + 1
        pos += 1
    return None, None


def extract_bbox(block):
    """Compute bounding box from all node coordinates in the block."""
    # Node format: (x,y,TYPE) where TYPE is like q, o, l, s, qs, ls, …
    matches = re.findall(r'\((-?\d+),(-?\d+),[qolsQOLS]+\)', block)
    if not matches:
        return None
    xs = [int(m[0]) for m in matches]
    ys = [int(m[1]) for m in matches]
    return min(xs), max(xs), min(ys), max(ys)


def build_anchors_existing(orig_bottom_pos, cx, min_y, max_x, cy):
    """Build anchors block for the modified existing vattu (adds bottom + right)."""
    bottom_y = min_y - 20
    return (
        f"anchors = (\n"
        f"{{\nname = _bottom;\npos = {orig_bottom_pos};\n}},\n"
        f"{{\nname = bottom;\npos = ({cx},{bottom_y});\n}},\n"
        f"{{\nname = right;\npos = ({max_x},{cy});\n}}\n"
        f");"
    )


def build_anchors_r(min_x, max_x, cy):
    """Build anchors block for the new vattu_r glyph (_right + right)."""
    return (
        f"anchors = (\n"
        f"{{\nname = _right;\npos = ({min_x},{cy});\n}},\n"
        f"{{\nname = right;\npos = ({max_x},{cy});\n}}\n"
        f");"
    )


# ── Read font ────────────────────────────────────────────────────────────────
with open(FONT_FILE, "r") as f:
    content = f.read()

# ── Pass 1: gather info about every vattu block ───────────────────────────────
glyph_data = {}   # consonant → (start, end, block, bbox, orig_bottom_pos)

for consonant in BLWF_ORDER:
    gname = f"{consonant}vattu-kannada"
    start, end = find_glyph_block(content, gname)
    if start is None:
        print(f"MISSING: {gname}")
        continue

    block = content[start:end]
    bbox = extract_bbox(block)
    if not bbox:
        print(f"NO NODES: {gname}")
        continue

    # Extract the original _bottom pos string, e.g. "(-306,33)"
    m = re.search(r'name = _bottom;\npos = (\([^)]+\));', block)
    if not m:
        print(f"NO _bottom: {gname}")
        continue

    glyph_data[consonant] = (start, end, block, bbox, m.group(1))
    min_x, max_x, min_y, max_y = bbox
    print(f"{gname}: [{min_x},{max_x}]x[{min_y},{max_y}]  _bottom={m.group(1)}")

print(f"\nFound {len(glyph_data)}/36 vattu glyphs\n")

# ── Pass 2: build replacement list (apply in reverse to preserve offsets) ─────
# Each entry: (start, end, replacement_text)
replacements = []

for consonant in BLWF_ORDER:
    if consonant not in glyph_data:
        continue
    start, end, block, bbox, orig_bottom_pos = glyph_data[consonant]
    min_x, max_x, min_y, max_y = bbox
    cx  = (min_x + max_x) // 2
    cy  = (min_y + max_y) // 2

    gname  = f"{consonant}vattu-kannada"
    r_name = f"{consonant}vattu_r-kannada"

    # ── A: modified existing vattu block ────────────────────────────────────
    anchors_re = re.compile(r'anchors = \(\n\{[^}]*\}\n\);')
    am = anchors_re.search(block)
    if not am:
        print(f"WARNING: anchors pattern not matched in {gname} — skipping")
        continue

    new_anchors = build_anchors_existing(orig_bottom_pos, cx, min_y, max_x, cy)
    new_block   = block[:am.start()] + new_anchors + block[am.end():]

    # ── B: vattu_r glyph block ───────────────────────────────────────────────
    r_block = block   # start from original (pre-modification)
    r_block = r_block.replace(f'glyphname = "{gname}";',
                               f'glyphname = "{r_name}";')
    r_block = re.sub(r'lastChange = "[^"]*";',
                     'lastChange = "2026-04-30 10:00:00 +0000";', r_block)
    # Strip fields that shouldn't carry over
    r_block = re.sub(r'\nunicode = \d+;', '', r_block)
    r_block = re.sub(r'\nnote = [^;]+;',  '', r_block)

    r_anchors = build_anchors_r(min_x, max_x, cy)
    r_block   = anchors_re.sub(r_anchors, r_block)

    # Replacement: original span → modified block + vattu_r block.
    # content[end:] already starts with "," (the separator to the next glyph),
    # so do NOT add a trailing comma here.
    replacements.append((start, end, new_block + f"\n{r_block}"))

# Apply in reverse order
replacements.sort(key=lambda x: x[0], reverse=True)
for s, e, text in replacements:
    content = content[:s] + text + content[e:]

print(f"Applied {len(replacements)} glyph edits\n")

# ── Pass 3: add vatu feature ──────────────────────────────────────────────────
vattu_glyphs   = " ".join(f"{c}vattu-kannada"   for c in BLWF_ORDER)
vattu_r_glyphs = " ".join(f"{c}vattu_r-kannada" for c in BLWF_ORDER)
sub_rules      = "\n".join(f"  sub {c}vattu-kannada by {c}vattu_r-kannada;" for c in BLWF_ORDER)

vatu_code = (
    "lookup vatu_right_sub {\n"
    f"{sub_rules}\n"
    "} vatu_right_sub;\n\n"
    "lookup vatu_right_ctx {\n"
    f"  sub [{vattu_glyphs} {vattu_r_glyphs}] [{vattu_glyphs}]' lookup vatu_right_sub;\n"
    "} vatu_right_ctx;"
)

# Insert vatu feature block right after the blwf feature block
blwf_tag = content.find('tag = blwf;')
if blwf_tag == -1:
    print("ERROR: tag = blwf; not found!")
else:
    blwf_block_end = content.find('},', blwf_tag)
    if blwf_block_end == -1:
        print("ERROR: couldn't find end of blwf feature block")
    else:
        vatu_block = (
            "\n{\n"
            f'code = "{vatu_code}";\n'
            "tag = vatu;\n"
            "},"
        )
        content = content[:blwf_block_end + 2] + vatu_block + content[blwf_block_end + 2:]
        print("Added vatu feature")

# ── Write back ────────────────────────────────────────────────────────────────
with open(FONT_FILE, "w") as f:
    f.write(content)

print("\nDone!")
