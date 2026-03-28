n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("3 and 5")
elif n % 3 == 0:
    print("3")
elif n % 5 == 0:
    print("5")
else:
    print("none")
