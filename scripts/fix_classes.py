import re

with open("Bilvafont-experiments.glyphs", "r") as f:
    content = f.read()

matras = [
    "aaMatra-kannada", "iMatra-kannada", "iiMatra-kannada", "uMatra-kannada",
    "uuMatra-kannada", "vocalicRMatra-kannada", "vocalicRRMatra-kannada",
    "vocalicLMatra-kannada", "vocalicLLMatra-kannada", "eMatra-kannada",
    "eeMatra-kannada", "aiMatra-kannada", "oMatra-kannada", "ooMatra-kannada",
    "auMatra-kannada"
]

classes_to_add = ""
for matra in matras:
    repeated = " ".join([matra] * 36)
    class_name = matra.replace("-kannada", "Class")
    classes_to_add += f",\n{{\ncode = \"{repeated}\";\nname = {class_name};\n}}"

old_str = 'name = auLigatures;\n}'
new_str = 'name = auLigatures;\n}' + classes_to_add

if old_str in content:
    content = content.replace(old_str, new_str)
    with open("Bilvafont-experiments.glyphs", "w") as f:
        f.write(content)
    print("Classes added successfully.")
else:
    print("Error: Could not find the anchor string.")
