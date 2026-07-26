from fontTools.ttLib import TTFont

font = TTFont("temp_orig.ttf")
hmtx = font["hmtx"]
for gn in ["uni0C82", "uni0C83", "uni0CD5"]:
    if gn in hmtx.metrics:
        print(f"Original TTF Glyph {gn}: width={hmtx.metrics[gn][0]}, lsb={hmtx.metrics[gn][1]}")
    else:
        print(f"Original TTF Glyph {gn} not in hmtx")
