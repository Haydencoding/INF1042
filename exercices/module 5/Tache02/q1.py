try:
    age = input("Entrez votre âge : ")

    if not age.isdigit():
        raise ValueError

    age = int(age)

    print(f"Vous avez {age} ans.")

except ValueError:
    print("Erreur : l'âge doit être un nombre entier.")
