# Nom: Hayden
# Description: calcule les frais de stationnement

heures = float(input("Combien d'heures de stationnement? "))
electrique = input("La voiture est electrique? oui ou non: ")

if heures <= 1:
    cout = 4
else:
    cout = 4 + (heures - 1) * 3

if heures > 5:
    cout = cout + 10

if electrique == "oui":
    cout = cout * 0.80

print("Le cout total est:", cout)
