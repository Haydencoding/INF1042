#Ce programme demande un nombre
#Calcule le carré du nombre choisi
#Affiche le résultat arrondi à 2 décimales

nombre = float(input("Entrez un nombre: "))
carre = pow(nombre, 2)
resultat = round(carre, 2)
print("Le carré est:", resultat)
