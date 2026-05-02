#!/usr/bin/env python3
"""
Script to add vocalic substitution rules to the 'pres' feature in Bilvafont-experiments.glyphs.
This covers vocalicRMatra, vocalicRRMatra, vocalicLMatra, and vocalicLLMatra.
"""

import re

FONT_FILE = "Bilvafont-experiments.glyphs"

CONSONANTS_36 = [
    "ka", "kha", "ga", "gha", "nga",
    "ca", "cha", "ja", "jha", "nya",
    "tta", "ttha", "dda", "ddha", "nna",
    "ta", "tha", "da", "dha", "na",
    "pa", "pha", "ba", "bha", "ma",
    "ya", "ra", "rra", "la", "va",
    "sha", "ssa", "sa", "ha", "lla", "llla"
]

MATRAS = [
    "vocalicRMatra",
    "vocalicRRMatra",
    "vocalicLMatra",
    "vocalicLLMatra"
]

def main():
    with open(FONT_FILE, "r") as f:
        content = f.read()

    # Generate the OpenType substitution rules
    rules = []
    for matra in MATRAS:
        rules.append(f"\n  # {matra} rules")
        for cons in CONSONANTS_36:
            base = f"{cons}-kannada"
            mark = f"{matra}-kannada"
            ligature = f"{cons}_{matra}-kannada"
            # Example output: sub ka-kannada vocalicRMatra-kannada by ka_vocalicRMatra-kannada;
            rules.append(f"  sub {base} {mark} by {ligature};")

    rules_str = "\n".join(rules)

    # Locate the `pres` feature block dynamically
    pres_pattern = re.compile(r'(code = ")(.*?)(";[\s\n]*tag = pres;)', re.DOTALL)
    match = pres_pattern.search(content)
    
    if not match:
        print("ERROR: Could not locate the 'pres' feature block in the font file.")
        return
        
    existing_code = match.group(2)
    if "vocalicRMatra rules" in existing_code:
        print("Rules already exist in the 'pres' feature. Aborting to prevent duplicates.")
        return

    new_code = existing_code + "\n" + rules_str + "\n"
    new_content = content[:match.start(1)] + 'code = "' + new_code + match.group(3) + content[match.end(3):]

    with open(FONT_FILE, "w") as f:
        f.write(new_content)
    
    print(f"Successfully added {len(MATRAS) * len(CONSONANTS_36)} vocalic ligature rules to the 'pres' feature.")

if __name__ == "__main__":
    main()
