# Question 2
produit = ("Clavier", 49.99, 12)
nom, prix, quantite = produit

print(nom, prix, quantite)
print(f"Le produit {nom} coûte {prix} $ et il y en a {quantite} en stock.")

produit2 = ("Souris", 29.99, 20)
nom2, prix2, _ = produit2

if prix > prix2:
    print(f"Le plus cher: {nom} à {prix} $")
else:
    print(f"Le plus cher: {nom2} à {prix2} $")
