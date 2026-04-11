nom = input("Entre ton nom : ")

while True:
    age = input("Entre ton âge : ")

    try:
        age = int(age)
        print(nom + ", dans 5 ans, tu auras", age + 5, "ans.")
        break
    except:
        print("Veuillez entrer un âge valide (nombre entier).")
