#!/usr/bin/env python3
"""
Script to increase the width of the 'space' glyph in Bilvafont-experiments.glyphs.
Requires glyphsLib: pip install glyphsLib
"""

import os
import glyphsLib

# Path assuming the script is run from the `scripts/` directory
FONT_FILE = "../sources/Bilvafont-experiments.glyphs"

# Set your desired space width here
NEW_WIDTH = 600 

def main():
    if not os.path.exists(FONT_FILE):
        print(f"ERROR: Could not find {FONT_FILE}. Make sure you run this from the 'scripts' directory.")
        return

    print(f"Loading {FONT_FILE}...")
    font = glyphsLib.load(FONT_FILE)

    if "space" not in font.glyphs:
        print("ERROR: 'space' glyph not found in the font.")
        return

    space_glyph = font.glyphs["space"]
    
    for layer in space_glyph.layers:
        old_width = layer.width
        layer.width = NEW_WIDTH
        print(f"Updated layer '{layer.name}' width: {old_width} -> {layer.width}")

    font.save(FONT_FILE)
    print("Changes saved successfully.")

if __name__ == "__main__":
    main()