#Ce programme vérifie si une personne peut entrer
#Retourne True si age >= 18

def peut_entrer(age):
    return age >= 18

age = int(input("Entrez votre âge : "))

if peut_entrer(age):
    print("Entrée autorisée")
else:
    print("Entrée refusée")
