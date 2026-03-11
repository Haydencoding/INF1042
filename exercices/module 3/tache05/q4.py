def valider_mot_de_passe(mot_de_passe):
    a_un_chiffre = any(caractere.isdigit() for caractere in mot_de_passe)
    a_une_lettre = any(caractere.isalpha() for caractere in mot_de_passe)
    assez_long = len(mot_de_passe) >= 8

    if a_un_chiffre and a_une_lettre and assez_long:
        return True
    else:
        return False


mot_de_passe = input("Entrez un mot de passe : ")

if valider_mot_de_passe(mot_de_passe):
    print("Mot de passe valide !")
else:
    print("Mot de passe invalide. Il doit contenir au moins 8 caractères, une lettre et un chiffre.")
