# Nom: Hayden
# Description: Ce programme calcule le prix final d'un achat
# avec un rabais et la taxe

prix = float(input("Entrez le prix d'achat: "))

if prix < 50:
    rabais = 0
elif prix <= 100:
    rabais = prix * 0.10
else:
    rabais = prix * 0.15

sous_total = prix - rabais
taxe = sous_total * 0.14975
total = sous_total + taxe

print("Prix original:", prix)
print("Rabais:", rabais)
print("Sous-total:", sous_total)
print("Taxe:", taxe)
print("Total:", total)