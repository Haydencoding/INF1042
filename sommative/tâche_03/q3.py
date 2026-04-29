# Question 3
liste_a = ["Batterie", "Basse", "Piano", "Basse", "Guitare", "Batterie"]
liste_b = ["Piano", "Voix", "Guitare", "Synthé", "Piano"]

a, b = set(liste_a), set(liste_b)

print("Uniques A:", a)
print("Uniques B:", b)
print("Dans les deux:", a & b)
print("Dans une seule:", a ^ b)
print("Toutes combinées:", a | b)
