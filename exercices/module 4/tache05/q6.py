matchs = (
    ("Tigres", "Lynx", 25, 18),
    ("Aigles", "Panthères", 22, 25),
    ("Tigres", "Panthères", 25, 23),
    ("Lynx", "Aigles", 19, 25),
    ("Tigres", "Aigles", 21, 25),
    ("Lynx", "Panthères", 25, 20)
)

victoires = {}
points = {}

# Initialiser
for e1, e2, _, _ in matchs:
    victoires[e1] = 0
    victoires[e2] = 0
    points[e1] = 0
    points[e2] = 0

# Parcourir les matchs
for e1, e2, s1, s2 in matchs:

    # Ajouter les points
    points[e1] += s1
    points[e2] += s2

    # Trouver le gagnant
    if s1 > s2:
        print("Les", e1, "ont battu les", e2, "par", s1, "à", s2)
        victoires[e1] += 1
    else:
        print("Les", e2, "ont battu les", e1, "par", s2, "à", s1)
        victoires[e2] += 1

# Résultats
print("\nVictoires :", victoires)
print("Points :", points)

# Équipe avec le plus de victoires
max_v = max(victoires.values())
for equipe in victoires:
    if victoires[equipe] == max_v:
        print("Meilleure équipe (victoires) :", equipe)

# Équipe avec le plus de points
max_p = max(points.values())
for equipe in points:
    if points[equipe] == max_p:
        print("Meilleure équipe (points) :", equipe)

# Victoires vs défaites
print("\nBilan :")
for equipe in victoires:
    defaites = 0

    for e1, e2, s1, s2 in matchs:
        if equipe == e1 and s1 < s2:
            defaites += 1
        if equipe == e2 and s2 < s1:
            defaites += 1

    if victoires[equipe] > defaites:
        print(equipe, ": plus de victoires")
    elif victoires[equipe] == defaites:
        print(equipe, ": égalité")
    else:
        print(equipe, ": plus de défaites")
