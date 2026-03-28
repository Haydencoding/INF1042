h = int(input())

if h == 0:
    print("12am")
elif h < 12:
    print(h, "am")
elif h == 12:
    print("12pm")
else:
    print(h - 12, "pm")
