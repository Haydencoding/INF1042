# Question 4
inventaire = {"stylos": 24, "cahiers": 15, "gommes": 10}

print(inventaire["cahiers"])
inventaire["marqueurs"] = 18
inventaire["stylos"] = 30
del inventaire["gommes"]

for produit, qte in inventaire.items():
    print(f"{produit}: {qte}")

print("Total:", sum(inventaire.values()))
