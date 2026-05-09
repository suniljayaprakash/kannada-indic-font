#MenuTitle: Copy bottom anchor from ka to ka_*Matra glyphs
# -*- coding: utf-8 -*-
"""
Copies the 'bottom' anchor from ka-kannada to all ka_*Matra-kannada
ligature glyphs, across every master in the font.

The 'bottom' anchor is used for below-base mark attachment (e.g. vattus).
Each ligature glyph needs the same anchor position as the base ka-kannada
so that vattus attach correctly when the ligature is the base glyph.

Usage: open font in Glyphs 3, then run via Script menu.
"""

font = Glyphs.font

if font is None:
    print("ERROR: No font is open.")
    raise SystemExit

SOURCE = "ka-kannada"
ANCHOR = "bottom"

source_glyph = font.glyphs[SOURCE]
if source_glyph is None:
    print(f"ERROR: '{SOURCE}' not found in font.")
    raise SystemExit

# All ka_*Matra-kannada and ka_halant-kannada ligature glyphs
targets = [
    g for g in font.glyphs
    if g.name.startswith("ka_")
    and ("Matra" in g.name or "halant" in g.name)
    and g.name.endswith("-kannada")
]

if not targets:
    print("ERROR: No ka_*Matra-kannada glyphs found.")
    raise SystemExit

targets.sort(key=lambda g: g.name)
print(f"Source : {SOURCE}")
print(f"Targets: {len(targets)} glyphs")
for g in targets:
    print(f"  {g.name}")
print()

copied = 0
skipped = 0

for master in font.masters:
    mid = master.id
    source_layer = source_glyph.layers[mid]

    if source_layer is None:
        print(f"[{master.name}] SKIP: no layer for '{SOURCE}'")
        skipped += 1
        continue

    src_anchor = next((a for a in source_layer.anchors if a.name == ANCHOR), None)
    if src_anchor is None:
        print(f"[{master.name}] SKIP: no '{ANCHOR}' anchor on '{SOURCE}'")
        skipped += 1
        continue

    x, y = src_anchor.position.x, src_anchor.position.y
    print(f"[{master.name}] '{ANCHOR}' at ({x:.0f}, {y:.0f}) — copying to {len(targets)} glyphs …")

    for glyph in targets:
        layer = glyph.layers[mid]
        if layer is None:
            print(f"  SKIP: no layer for '{glyph.name}'")
            skipped += 1
            continue

        # Remove any existing anchor with this name
        for existing in list(layer.anchors):
            if existing.name == ANCHOR:
                layer.anchors.remove(existing)

        # Add the copied anchor
        new_anchor = GSAnchor()
        new_anchor.name = ANCHOR
        new_anchor.position = (x, y)
        layer.anchors.append(new_anchor)

        print(f"  ✓ {glyph.name}")
        copied += 1

print(f"\nDone. {copied} anchor(s) set, {skipped} skipped.")
