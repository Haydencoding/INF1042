valeurs = []

# Ouvrir le fichier en lecture
with open("valeurs.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        valeurs.append(int(ligne.strip()))

# Calculs
maximum = max(valeurs)
minimum = min(valeurs)
moyenne = sum(valeurs) / len(valeurs)

# Affichage
print("Maximum :", maximum)
print("Minimum :", minimum)
print("Moyenne :", moyenne)
