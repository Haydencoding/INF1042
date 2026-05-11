try:
    note1 = float(input("Note 1 : "))
    note2 = float(input("Note 2 : "))

    if note1 < 0 or note1 > 100 or note2 < 0 or note2 > 100:
        raise ValueError("note")

except ValueError as erreur:
    if str(erreur) == "note":
        print("Erreur : les notes doivent être entre 0 et 100.")
    else:
        print("Erreur : les notes doivent être numériques.")

else:
    moyenne = (note1 + note2) / 2
    print(f"Moyenne : {moyenne}")

finally:
    print("Fin du programme.")
