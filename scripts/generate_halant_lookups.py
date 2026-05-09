#!/usr/bin/env python3
"""
Generates OpenType feature code for halant fallback lookups using 
a Mark Filtering Set, which allows the shaping engine to skip Vattus.
"""

CONSONANTS_36 = [
    "ka", "kha", "ga", "gha", "nga", "ca", "cha", "ja", "jha", "nya",
    "tta", "ttha", "dda", "ddha", "nna", "ta", "tha", "da", "dha", "na",
    "pa", "pha", "ba", "bha", "ma", "ya", "ra", "rra", "la", "va",
    "sha", "ssa", "sa", "ha", "lla", "llla"
]

print("lookup half_forms_fallback {")
print("  # This filtering set ensures we skip over Vattus (which are Marks)")
print("  # so consonant_1 and the final halant can combine successfully.")
print("  lookupflag UseMarkFilteringSet @HalantOnly;")
print()
for cons in CONSONANTS_36:
    print(f"  sub {cons}-kannada halant-kannada by {cons}_halant-kannada;")
print("} half_forms_fallback;")