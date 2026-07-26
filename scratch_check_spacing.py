import ufoLib2

font = ufoLib2.Font.open("sources/Nanni-Regular.ufo")
for gn in ["uni0C82", "uni0C83", "uni0CD5"]:
    g = font[gn]
    print(f"Glyph {gn}:")
    print(f"  Width: {g.width}")
    print(f"  Contours: {len(g)}")
    print(f"  Anchors: {[ (a.name, a.x, a.y) for a in g.anchors ]}")
