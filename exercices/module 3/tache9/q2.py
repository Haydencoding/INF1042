import random
import time

nb = int(input("Combien de questions: "))

correct = 0
incorrect = 0

start_total = time.time()

for i in range(nb):
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    op = random.choice(["+", "-", "*", "/"])

    question = str(a) + " " + op + " " + str(b)
    start = time.time()

    rep = float(input(question + " = "))

    end = time.time()

    if op == "+":
        bonne = a + b
    elif op == "-":
        bonne = a - b
    elif op == "*":
        bonne = a * b
    else:
        bonne = a / b

    if rep == bonne:
        print("Correct")
        correct += 1
    else:
        print("Faux (reponse:", bonne, ")")
        incorrect += 1

    print("Temps:", round(end - start, 2), "sec\n")

end_total = time.time()

print("Total correct:", correct)
print("Total incorrect:", incorrect)
print("Temps total:", round(end_total - start_total, 2), "sec")
