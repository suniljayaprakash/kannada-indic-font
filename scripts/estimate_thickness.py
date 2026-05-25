#!/usr/bin/env python3
import re
import numpy as np

FONT_FILE = "sources/Glyphs/Nanni-2.0.glyphs"
NODE_RE = re.compile(r'\((-?\d+),(-?\d+),([a-zA-Z\d]+)\)')

def find_glyph_block(content, glyph_name):
    for needle in [f'glyphname = {glyph_name};', f'glyphname = "{glyph_name}";']:
        idx = content.find(needle)
        if idx != -1:
            pos = idx - 1
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

def get_paths(content, glyph_name):
    start, end = find_glyph_block(content, glyph_name)
    if start is None:
        return []
    block = content[start:end]
    shapes_idx = block.find("shapes = (")
    if shapes_idx == -1:
        return []
    shapes_content = block[shapes_idx:]
    depth = 0
    s_end = 0
    for i, char in enumerate(shapes_content):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth == 0:
                s_end = i + 1
                break
    shapes_block = shapes_content[:s_end]
    
    paths = []
    pos = 0
    while True:
        p_start = shapes_block.find("{", pos)
        if p_start == -1:
            break
        depth = 0
        p_end = p_start
        while p_end < len(shapes_block):
            if shapes_block[p_end] == '{':
                depth += 1
            elif shapes_block[p_end] == '}':
                depth -= 1
                if depth == 0:
                    p_end += 1
                    break
            p_end += 1
        paths.append(shapes_block[p_start:p_end])
        pos = p_end
        
    res = []
    for p in paths:
        nodes = []
        for m in NODE_RE.finditer(p):
            nodes.append((int(m.group(1)), int(m.group(2)), m.group(3)))
        res.append(nodes)
    return res

def get_left_loop_thickness(paths):
    # Let's find the main path (consonant body)
    main_path = max(paths, key=len)
    
    # We want to measure thickness of the left loop.
    # The left loop has nodes on the outer edge (e.g. X near 44) and inner edge.
    # Let's find pairs of nodes that have similar Y but different X.
    # Specifically, around Y = 250 (which is the middle of the loop).
    outer_left = None
    inner_left = None
    inner_right = None
    outer_right = None
    
    # Let's look at nodes with Y in [200, 300] and X < 450
    candidates = [n for n in main_path if 200 <= n[1] <= 300 and n[0] < 450]
    
    # Sort candidates by X coordinate
    candidates.sort(key=lambda n: n[0])
    
    # Let's print candidates to see if we can identify the four edges of the loop:
    # Outer Left, Inner Left, Inner Right, Outer Right
    print("Candidates sorted by X:")
    for c in candidates:
        print(f"  {c}")

def main():
    with open(FONT_FILE) as f:
        content = f.read()
        
    print("=== uni0CAE (MA) ===")
    get_left_loop_thickness(get_paths(content, "uni0CAE"))
    
    print("\n=== uniE720 (MI) ===")
    get_left_loop_thickness(get_paths(content, "uniE720"))

if __name__ == "__main__":
    main()
