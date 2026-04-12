import random

# Création et écriture dans le fichier
with open("valeurs.txt", "w", encoding="utf-8") as f:
    for _ in range(1000):
        nombre = random.randint(0, 100000)
        f.write(str(nombre) + "\n")

print("Fichier valeurs.txt créé avec 1000 valeurs.")
