# Nom: Hayden
# Description: simule des nombres aleatoires entre 1 et 4

import random

n = int(input("Combien de valeurs? "))

c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in range(n):
    val = random.randint(1, 4)
    if val == 1:
        c1 = c1 + 1
    elif val == 2:
        c2 = c2 + 1
    elif val == 3:
        c3 = c3 + 1
    else:
        c4 = c4 + 1

print("Valeur 1:", c1, "fois", c1/n*100, "%")
print("Valeur 2:", c2, "fois", c2/n*100, "%")
print("Valeur 3:", c3, "fois", c3/n*100, "%")
print("Valeur 4:", c4, "fois", c4/n*100, "%")