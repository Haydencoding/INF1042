import random
import string

# demander infos
prenom = input("Prenom: ")
nom = input("Nom: ")
annee = int(input("Annee de naissance: "))
ville = input("Ville: ")

# username
username = prenom.lower() + "." + nom.lower()
email = username + "@" + ville.lower() + ".ca"

# age
age = 2026 - annee
if age >= 18:
    print("18 ans ou plus")
else:
    print("Moins de 18 ans")

# mot de passe
part1 = prenom[:2]
part2 = nom[-2:]
part3 = str(annee)

chars = string.ascii_letters + string.digits
random_part = ""
for i in range(4):
    random_part += random.choice(chars)

password = part1 + part2 + part3 + random_part

print("Username:", username)
print("Email:", email)
print("Password:", password)
