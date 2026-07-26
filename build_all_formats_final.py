import subprocess
import os
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_a_s_p import table__g_a_s_p
from fontTools.ttLib.tables._p_r_e_p import table__p_r_e_p
from fontTools.ttLib.tables.ttProgram import Program

ufo_path = "sources/Nanni-Regular.ufo"
builds_dir = "docs/builds"

ttf_path = os.path.join(builds_dir, "Nanni-Regular.ttf")
otf_path = os.path.join(builds_dir, "Nanni-Regular.otf")
woff_path = os.path.join(builds_dir, "Nanni-Regular.woff")
woff2_path = os.path.join(builds_dir, "Nanni-Regular.woff2")

# List of zero-width glyphs that need GDEF Class 3 override
gdef_marks = ["uni0CC1", "uni0CC8", "uni0CD5", "uni0C80", "uni0C82", "uni0C83", "uni0CF3"]

print("1. COMPILING TTF...")
cmd_ttf = [
    ".venv/bin/fontmake",
    "-u", ufo_path,
    "-o", "ttf",
    "--keep-overlaps",
    "--output-path", ttf_path
]
subprocess.run(cmd_ttf, check=True)

print("2. POST-PROCESSING TTF...")
ttf_font = TTFont(ttf_path)

if "gasp" in ttf_font:
    del ttf_font["gasp"]
gasp = table__g_a_s_p()
gasp.gaspRange = {65535: 15}
ttf_font["gasp"] = gasp

if "prep" in ttf_font:
    del ttf_font["prep"]
prep = table__p_r_e_p()
program = Program()
program.fromBytecode(b'\xb8\x01\xff\x85\xb0\x04\x8d')
prep.program = program
ttf_font["prep"] = prep

if "GDEF" in ttf_font and ttf_font["GDEF"].table and ttf_font["GDEF"].table.GlyphClassDef:
    class_defs = ttf_font["GDEF"].table.GlyphClassDef.classDefs
    for gn in gdef_marks:
        class_defs[gn] = 3
        print(f"  Set TTF GDEF class for {gn} to 3 (Mark)")
else:
    print("  Warning: GDEF table or GlyphClassDef not found in built TTF!")
if "OS/2" in ttf_font:
    ttf_font["OS/2"].fsSelection |= (1 << 7)
    print("  Set OS/2.fsSelection bit 7 (USE_TYPO_METRICS) on TTF")

ttf_font.save(ttf_path)

print("3. GENERATING WOFF AND WOFF2...")
post_ttf = TTFont(ttf_path)
post_ttf.flavor = "woff"
post_ttf.save(woff_path)
post_ttf.flavor = "woff2"
post_ttf.save(woff2_path)
print("WOFF & WOFF2 generated successfully.")

print("4. COMPILING OTF...")
cmd_otf = [
    ".venv/bin/fontmake",
    "-u", ufo_path,
    "-o", "otf",
    "--keep-overlaps",
    "--output-path", otf_path
]
subprocess.run(cmd_otf, check=True)

print("5. POST-PROCESSING OTF...")
otf_font = TTFont(otf_path)
if "GDEF" in otf_font and otf_font["GDEF"].table and otf_font["GDEF"].table.GlyphClassDef:
    class_defs = otf_font["GDEF"].table.GlyphClassDef.classDefs
    for gn in gdef_marks:
        class_defs[gn] = 3
        print(f"  Set OTF GDEF class for {gn} to 3 (Mark)")
else:
    print("  Warning: GDEF table or GlyphClassDef not found in built OTF!")

if "OS/2" in otf_font:
    otf_font["OS/2"].fsSelection |= (1 << 7)
    print("  Set OS/2.fsSelection bit 7 (USE_TYPO_METRICS) on OTF")

otf_font.save(otf_path)

print("ALL FORMATS REBUILT SUCCESSFULLY!")
