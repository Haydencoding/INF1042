a = float(input("Entrez côté 1: "))
b = float(input("Entrez côté 2: "))
c = float(input("Entrez côté 3: "))

if a + b > c and a + c > b and b + c > a:
    print(True)
else:
    print(False)
