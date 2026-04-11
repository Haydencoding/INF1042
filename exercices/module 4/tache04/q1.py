notes = [12, 15, 9, 18, 15, 12]

# Moyenne
moyenne = sum(notes) / len(notes)
print("Moyenne :", float(moyenne))

# Trouver la valeur la plus fréquente
max_count = 0
valeur_freq = None

for n in notes:
    count = notes.count(n)
    if count > max_count:
        max_count = count
        valeur_freq = n

print("Valeur la plus fréquente :", valeur_freq)
