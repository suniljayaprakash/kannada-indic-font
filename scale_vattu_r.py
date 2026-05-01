#!/usr/bin/env python3
"""
Scale all *vattu_r-kannada glyph nodes and anchors by SCALE_FACTOR.
Anchors (_right, right) are recomputed from the new bounding box.
"""

import re

FONT_FILE = "Bilvafont-experiments.glyphs"
SCALE = 0.70   # 70% of original size

BLWF_ORDER = [
    "ka", "kha", "ga", "gha", "nga",
    "ca", "cha", "ja", "jha", "nya",
    "tta", "ttha", "dda", "ddha", "nna",
    "ta", "tha", "da", "dha", "na",
    "pa", "pha", "ba", "bha", "ma",
    "ya", "ra", "rra", "la", "va",
    "sha", "ssa", "sa", "ha", "lla", "llla",
]

# ── node pattern: (x,y,TYPE)  where TYPE ∈ {q,o,l,s,qs,ls,…} ────────────────
NODE_RE = re.compile(r'\((-?\d+),(-?\d+),([qolsQOLS]+)\)')

def find_glyph_block(content, glyph_name):
    needle = f'glyphname = "{glyph_name}";'
    name_idx = content.find(needle)
    if name_idx == -1:
        return None, None
    pos = name_idx - 1
    while pos >= 0 and content[pos] != '{':
        pos -= 1
    block_start = pos
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


def scale_nodes(block):
    """Scale every node coordinate by SCALE and return the modified block."""
    def replace_node(m):
        x = round(int(m.group(1)) * SCALE)
        y = round(int(m.group(2)) * SCALE)
        return f'({x},{y},{m.group(3)})'
    return NODE_RE.sub(replace_node, block)


def recompute_anchors(block):
    """
    After scaling, recompute _right and right anchors from the new bounding box.
    Replaces the entire anchors = (...); section.
    """
    coords = [(int(m.group(1)), int(m.group(2))) for m in NODE_RE.finditer(block)]
    if not coords:
        return block
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    min_x, max_x = min(xs), max(xs)
    cy = (min(ys) + max(ys)) // 2

    new_anchors = (
        f"anchors = (\n"
        f"{{\nname = _right;\npos = ({min_x},{cy});\n}},\n"
        f"{{\nname = right;\npos = ({max_x},{cy});\n}}\n"
        f");"
    )
    return re.sub(r'anchors = \(\n\{[^}]*\},\n\{[^}]*\}\n\);', new_anchors, block)


# ── main ──────────────────────────────────────────────────────────────────────
with open(FONT_FILE) as f:
    content = f.read()

replacements = []   # (start, end, new_text)

for consonant in BLWF_ORDER:
    r_name = f"{consonant}vattu_r-kannada"
    start, end = find_glyph_block(content, r_name)
    if start is None:
        print(f"MISSING: {r_name}")
        continue

    block = content[start:end]
    scaled = scale_nodes(block)
    scaled = recompute_anchors(scaled)
    replacements.append((start, end, scaled))
    print(f"Scaled {r_name}")

# Apply in reverse order to preserve offsets
replacements.sort(key=lambda x: x[0], reverse=True)
for s, e, text in replacements:
    content = content[:s] + text + content[e:]

with open(FONT_FILE, "w") as f:
    f.write(content)

print(f"\nDone — scaled {len(replacements)} glyphs to {int(SCALE*100)}%")
