solde = 250.00

try:
    montant = float(input("Montant à retirer : "))

    if montant <= 0:
        raise ValueError("negatif")

    if montant > solde:
        raise ValueError("fonds")

except ValueError as erreur:
    if str(erreur) == "fonds":
        print("Erreur : fonds insuffisants.")
    elif str(erreur) == "negatif":
        print("Erreur : le montant doit être supérieur à 0.")
    else:
        print("Erreur : le montant doit être numérique.")

else:
    solde -= montant
    print("Retrait accepté.")
    print(f"Nouveau solde : {solde:.2f} $")

finally:
    print("Fin de la transaction.")
