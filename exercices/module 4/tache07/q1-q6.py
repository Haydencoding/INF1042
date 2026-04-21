eleve = {
    "nom": "Alex",
    "age": 16,
    "programme": "Informatique"
}

notes = {"math": 78, "Français": 85, "science": 91}

print(notes["science"])

notes["histoire"] = 88
notes["math"] = 82

for matiere, note in notes.items():
    print("Matière:", matiere, "| Note:", note)

mots = ["chat", "chien", "chat", "oiseau", "chien", "chat"]

compte = {}

for mot in mots:
    if mot in compte:
        compte[mot] += 1
    else:
        compte[mot] = 1

print(compte)
