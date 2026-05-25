import glyphsLib

FONT_PATH = "sources/Glyphs/Nanni-2.0.glyphs"

def main():
    print(f"Loading {FONT_PATH}...")
    font = glyphsLib.load(FONT_PATH)
    
    modified_count = 0
    for glyph in font.glyphs:
        if glyph.name.endswith(".below") or glyph.name.endswith(".below.following"):
            # Set to Mark and Nonspacing
            glyph.category = "Mark"
            glyph.subCategory = "Nonspacing"
            print(f"Set category/subCategory for: {glyph.name}")
            modified_count += 1
            
    if modified_count > 0:
        print(f"Saving modified font back to {FONT_PATH} ({modified_count} glyphs updated)...")
        # Save the font
        font.save(FONT_PATH)
        print("Font saved successfully.")
    else:
        print("No matching glyphs found.")

if __name__ == "__main__":
    main()
