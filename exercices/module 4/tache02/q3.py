with open("valeurs.txt", "r", encoding="utf-8") as f, \
     open("bas.txt", "w", encoding="utf-8") as bas, \
     open("haut.txt", "w", encoding="utf-8") as haut:

    for ligne in f:
        valeur = int(ligne.strip())

        if 0 <= valeur <= 49999:
            bas.write(str(valeur) + "\n")
        else:
            haut.write(str(valeur) + "\n")

print("Fichiers bas.txt et haut.txt créés.")
