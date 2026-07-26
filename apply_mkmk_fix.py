fea_path = "sources/Nanni-Regular.ufo/features.fea"
print(f"Reading {fea_path}...")
with open(fea_path, "r") as f:
    content = f.read()

target = """feature mkmk {
### open feature 'mkmk' ###
	lookup mkmk_DFLT_vattu {
		lookupflag UseMarkFilteringSet @anchor_vattu;
		pos mark vocalicLLMatra_kannada.below.following <anchor 451 0> mark @mark_vattu;
		pos mark uni0CE2.following <anchor 416 0> mark @mark_vattu;
	} mkmk_DFLT_vattu;
### close feature 'mkmk' ###
} mkmk;"""

replacement = """feature mkmk {
### open feature 'mkmk' ###
	lookup mkmk_DFLT_vattu {
		lookupflag UseMarkFilteringSet @anchor_vattu;
		pos mark vocalicLLMatra_kannada.below.following <anchor 451 0> mark @mark_vattu;
		pos mark uni0CE2.following <anchor 416 0> mark @mark_vattu;
	} mkmk_DFLT_vattu;
	lookup mkmk_uppervedictone {
		lookupflag UseMarkFilteringSet @anchor_uppervedictone;
		pos mark uni0CF3 <anchor 211 1200> mark @mark_uppervedictone;
		pos mark uni0C82 <anchor 274 550> mark @mark_uppervedictone;
	} mkmk_uppervedictone;
### close feature 'mkmk' ###
} mkmk;"""

if target in content:
    content = content.replace(target, replacement)
    print("Successfully replaced mkmk block.")
else:
    # Let's do a re-based search with fewer whitespace assumptions
    import re
    pattern = r"feature\s+mkmk\s*\{\s*###\s*open\s+feature\s+'mkmk'\s*###\s*lookup\s+mkmk_DFLT_vattu\s*\{\s*lookupflag\s+UseMarkFilteringSet\s+@anchor_vattu\s*;\s*pos\s+mark\s+vocalicLLMatra_kannada\.below\.following\s+<anchor\s+451\s+0>\s+mark\s+@mark_vattu\s*;\s*pos\s+mark\s+uni0CE2\.following\s+<anchor\s+416\s+0>\s+mark\s+@mark_vattu\s*;\s*\}\s*mkmk_DFLT_vattu\s*;\s*###\s*close\s+feature\s+'mkmk'\s*###\s*\}\s*mkmk\s*;"
    content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    print(f"Replaced {count} occurrences via regex.")

with open(fea_path, "w") as f:
    f.write(content)
print("Done.")
