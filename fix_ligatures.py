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
    "aaLigatures": "aaMatra",
    "iLigatures": "iMatra",
    "iiLigatures": "iiMatra",
    "uLigatures": "uMatra",
    "uuLigatures": "uuMatra",
    "eLigatures": "eMatra",
    "eeLigatures": "eeMatra",
    "aiLigatures": "aiMatra",
    "oLigatures": "oMatra",
    "ooLigatures": "ooMatra",
    "auLigatures": "auMatra",
    "vocRLigatures": "vocalicRMatra",
    "vocRRLigatures": "vocalicRRMatra",
    "vocLLigatures": "vocalicLMatra",
    "vocLLLigatures": "vocalicLLMatra"
}

for lig_class, matra_name in matras.items():
    ligatures = [c.replace("-kannada", f"_{matra_name}-kannada") for c in consonants]
    ligatures_str = " ".join(ligatures)
    
    # Check if the class exists in the file
    match = re.search(r'code = "(.*?)";\nname = ' + lig_class + r';', content, re.DOTALL)
    if match:
        content = content[:match.start(1)] + ligatures_str + content[match.end(1):]
    else:
        print(f"Warning: {lig_class} not found.")

with open("Bilvafont-experiments.glyphs", "w") as f:
    f.write(content)

print("Ligature classes fixed.")
