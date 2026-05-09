import re

with open("Bilvafont-experiments.glyphs", "r") as f:
    content = f.read()

consonants_match = re.search(r'code = "(.*?)";\nname = Consonants;', content, re.DOTALL)
if consonants_match:
    consonants = consonants_match.group(1).split()
else:
    print("Consonants not found!")
    exit(1)

matras = {
    "vocRLigatures": "vocalicRMatra",
    "vocRRLigatures": "vocalicRRMatra",
    "vocLLigatures": "vocalicLMatra",
    "vocLLLigatures": "vocalicLLMatra"
}

classes_to_add = ""
for lig_class, matra_name in matras.items():
    ligatures = [c.replace("-kannada", f"_{matra_name}-kannada") for c in consonants]
    ligatures_str = " ".join(ligatures)
    classes_to_add += f",\n{{\ncode = \"{ligatures_str}\";\nname = {lig_class};\n}}"

old_str = 'name = auMatraClass;\n}'
new_str = 'name = auMatraClass;\n}' + classes_to_add

if old_str in content:
    content = content.replace(old_str, new_str)
    with open("Bilvafont-experiments.glyphs", "w") as f:
        f.write(content)
    print("Missing ligature classes added.")
else:
    print("Error: Could not find the anchor string.")
