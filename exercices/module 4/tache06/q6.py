import random

eleves = {"Maksym", "Léo", "Hayden", "Angel", "Ibrahim", "Josh", "Grant", "Maxime", "David"}

liste = list(eleves)

random.shuffle(liste)

for nom in liste:
    print(nom)
