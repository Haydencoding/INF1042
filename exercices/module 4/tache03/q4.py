texte = """Dans un coin oublié d’un vieux laboratoire, vivait un petit ordinateur gris..."""

# Nettoyer la ponctuation
texte = texte.lower()
texte = texte.replace(",", "").replace(".", "").replace("!", "").replace(":", "").replace(";", "").replace("’", "").replace("'", "")

mots = texte.split()

compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

print(compteur)
