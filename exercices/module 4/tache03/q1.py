import random

# Liste avec doublons
liste = [random.randint(1, 20) for _ in range(100)]

# Enlever doublons avec set
sans_doublons = set(liste)

# Revenir en liste triée
liste_triee = sorted(list(sans_doublons))

print("Liste originale :", liste)
print("Sans doublons :", sans_doublons)
print("Liste triée :", liste_triee)
