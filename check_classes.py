import re

with open("Bilvafont-experiments.glyphs", "r") as f:
    content = f.read()

def get_class(name):
    match = re.search(r'code = "(.*?)";\nname = ' + name + r';', content, re.DOTALL)
    if match:
        return match.group(1).split()
    return []

cons = get_class("Consonants")
print(f"Consonants length: {len(cons)}")

ligatures = ["aaLigatures", "iLigatures", "iiLigatures", "uLigatures", "uuLigatures", "eLigatures", "eeLigatures", "aiLigatures", "oLigatures", "ooLigatures", "auLigatures"]
for lig in ligatures:
    l = get_class(lig)
    print(f"{lig} length: {len(l)}")

