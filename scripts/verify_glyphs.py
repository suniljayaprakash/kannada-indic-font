#!/usr/bin/env python3
import sys
import glyphsLib

FONT_PATH = "../sources/Glyphs/Nanni-2.0.glyphs"

TARGETS = [
    "uni0CC3",
    "uni0CC4",
    "vocalicLMatra-kannada",
    "vocalicLLMatra-kannada"
]

def main():
    print(f"Loading {FONT_PATH} using glyphsLib...")
    try:
        font = glyphsLib.load(FONT_PATH)
    except Exception as e:
        print(f"ERROR loading font: {e}")
        sys.exit(1)

    print("\nVerifying glyph widths in the loaded font object:")
    print("-" * 50)
    for glyph_name in TARGETS:
        try:
            glyph = font.glyphs[glyph_name]
        except KeyError:
            print(f"ERROR: Glyph '{glyph_name}' not found in the font.")
            continue
        
        # print widths across all layers/masters
        for layer in glyph.layers:
            # Only print for masters (associated with a master ID)
            if layer.associatedMasterId:
                master = font.masters[layer.associatedMasterId]
                print(f"Glyph: {glyph_name:<25} | Master: {master.name:<15} | Width: {layer.width}")
    print("-" * 50)

if __name__ == "__main__":
    main()
