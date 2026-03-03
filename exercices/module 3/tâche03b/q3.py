temperature = float(input("Température: "))
pluie = input("Pluie (oui/non): ")

if temperature >= 15 and pluie == "non":
    print("Sortie permise")
else:
    print("On reste dedans")
