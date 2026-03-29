# Nom: Hayden
# Description: jeu pierre papier ciseaux contre l'ordinateur

import random

victoires = 0
defaites = 0
egalites = 0

while True:
    joueur = input("Choisissez pierre, papier ou ciseaux: ")
    ordi = random.choice(["pierre", "papier", "ciseaux"])

    print("L'ordinateur a choisi:", ordi)

    if joueur == ordi:
        print("Egalite!")
        egalites = egalites + 1
    elif joueur == "pierre" and ordi == "ciseaux":
        print("Vous avez gagnez!")
        victoires = victoires + 1
    elif joueur == "papier" and ordi == "pierre":
        print("Vous avez gagnez!")
        victoires = victoires + 1
    elif joueur == "ciseaux" and ordi == "papier":
        print("Vous avez gagnez!")
        victoires = victoires + 1
    else:
        print("Vous avez perdu!")
        defaites = defaites + 1

    print("Victoires:", victoires, "Defaites:", defaites, "Egalites:", egalites)

    continuer = input("Voulez-vous continuer? oui ou non: ")
    if continuer == "non":
        break