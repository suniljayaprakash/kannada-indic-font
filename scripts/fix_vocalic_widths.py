#!/usr/bin/env python3
import os
import re

FONT_PATH = "../sources/Glyphs/Nanni-2.0.glyphs"

TARGETS = {
    "uni0CC3": 175,
    "uni0CC4": 340,
    "vocalicLMatra-kannada": 210,
    "vocalicLLMatra-kannada": 244
}

def main():
    if not os.path.exists(FONT_PATH):
        print(f"ERROR: Font file not found at {FONT_PATH}")
        return

    print(f"Reading {FONT_PATH}...")
    with open(FONT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    modified_count = 0
    
    # Process each target glyph
    for glyph_name, target_width in TARGETS.items():
        # Find the glyph block. We match glyphname, and then the following layer and its width.
        # Format can be: glyphname = name; or glyphname = "name";
        # We search for the pattern starting with glyphname and ending around unicode/note/closing brace.
        # But to be extremely safe, we can use a regex that matches the glyph definition block.
        # Since glyph definitions in Glyphs format look like:
        # {
        # glyphname = <name>; (or "<name>")
        # ...
        # layers = (
        # {
        # ...
        # width = 0;
        # }
        # );
        # ...
        # }
        
        # Pattern explanation:
        # - {\s*[^}]*?glyphname\s*=\s*(?:"glyph_name"|glyph_name)\s*;
        # - matches everything non-greedy until we find `width = 0;` inside layers.
        # Wait, since layers themselves have braces, a simple non-greedy [^}]*? might stop early.
        # Let's match: `glyphname\s*=\s*(?:"?{glyph_name}"?)\s*;`
        # and then find the next `width\s*=\s*0\s*;` within a reasonable range before the next `glyphname` or closing block.
        
        # Let's search for the position of `glyphname = <glyph_name>;`
        escaped_name = re.escape(glyph_name)
        pattern = rf'glyphname\s*=\s*["\']?{escaped_name}["\']?\s*;'
        match = re.search(pattern, content)
        
        if not match:
            print(f"WARNING: Glyph '{glyph_name}' not found.")
            continue
            
        start_idx = match.start()
        # Find the next `width = 0;` after this start_idx
        # We want to make sure we don't scan into the next glyph block.
        # A glyph block usually ends before another `glyphname =` starts.
        next_glyph_match = re.search(r'glyphname\s*=', content[start_idx + len(match.group(0)):])
        end_boundary = len(content) if not next_glyph_match else start_idx + len(match.group(0)) + next_glyph_match.start()
        
        # Now search for `width = 0;` in the range [start_idx, end_boundary]
        width_pattern = re.compile(r'width\s*=\s*0\s*;')
        width_match = width_pattern.search(content, start_idx, end_boundary)
        
        if not width_match:
            # Let's check if it already has a non-zero width
            any_width_match = re.compile(r'width\s*=\s*(\d+)\s*;').search(content, start_idx, end_boundary)
            if any_width_match:
                print(f"Glyph '{glyph_name}' already has width = {any_width_match.group(1)}.")
            else:
                print(f"WARNING: Could not find width definition for '{glyph_name}' in its block.")
            continue
            
        # Replace the `width = 0;` with `width = <target_width>;`
        w_start, w_end = width_match.span()
        new_width_str = f"width = {target_width};"
        content = content[:w_start] + new_width_str + content[w_end:]
        print(f"Updated '{glyph_name}' width: 0 -> {target_width}")
        modified_count += 1

    if modified_count > 0:
        print(f"Writing changes back to {FONT_PATH}...")
        with open(FONT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done!")
    else:
        print("No changes made.")

if __name__ == "__main__":
    main()
