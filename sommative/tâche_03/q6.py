# Question 6
achats = [
    ("Liam",   "Galaxy Battle", "PC",          59.99),
    ("Emma",   "Speed Zone",    "PlayStation",  49.99),
    ("Liam",   "Pixel Quest",   "Switch",       39.99),
    ("Noah",   "Galaxy Battle", "PC",           59.99),
    ("Emma",   "Sky Builder",   "PC",           29.99),
    ("Olivia", "Speed Zone",    "Xbox",         54.99),
    ("Liam",   "Sky Builder",   "PC",           29.99),
    ("Noah",   "Pixel Quest",   "Switch",       39.99),
]

for a in achats:
    print(f"{a[0]} | {a[1]} | {a[2]} | {a[3]} $")

jeux = {a[1] for a in achats}
plateformes = {a[2] for a in achats}
print("Jeux:", jeux)
print("Plateformes:", plateformes)
print("Total dépensé:", sum(a[3] for a in achats))

depenses = {}
for a in achats:
    depenses[a[0]] = depenses.get(a[0], 0) + a[3]
print("Dépenses par client:", depenses)
print("Client top:", max(depenses, key=depenses.get))

comptage = {}
for a in achats:
    comptage[a[1]] = comptage.get(a[1], 0) + 1
print("Achats par jeu:", comptage)

print("Achats PC:")
for a in achats:
    if a[2] == "PC":
        print(f"  {a[0]} - {a[1]} - {a[3]} $")

print("RÉSUMÉ")
print(f"Nombre d'achats : {len(achats)}")
print(f"Jeux uniques    : {jeux}")
print(f"Plateformes     : {plateformes}")
print(f"Client top      : {max(depenses, key=depenses.get)}")
print(f"Jeu plus acheté : {max(comptage, key=comptage.get)}")
