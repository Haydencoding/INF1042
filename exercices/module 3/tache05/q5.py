notes = []

while True:
    print("\nGestionnaire de notes")
    print("1. Entrer des notes")
    print("2. Calculer la moyenne")
    print("3. Compter les notes de réussite (>= 50)")
    print("4. Compter les notes d'échec (< 50)")
    print("5. Quitter")

    choix = input("\nChoisissez une option : ")

    if choix == "1":
        quantite = int(input("Combien de notes voulez-vous entrer ? "))
        for i in range(quantite):
            note = float(input(f"Entrez la note {i + 1} : "))
            notes.append(note)
        print("Notes sauvegardées !")

    elif choix == "2":
        if len(notes) == 0:
            print("Aucune note entrée pour l'instant.")
        else:
            moyenne = sum(notes) / len(notes)
            print(f"Moyenne : {moyenne:.2f}")

    elif choix == "3":
        reussites = sum(1 for n in notes if n >= 50)
        print(f"Notes de réussite : {reussites}")

    elif choix == "4":
        echecs = sum(1 for n in notes if n < 50)
        print(f"Notes d'échec : {echecs}")

    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("Option invalide, essayez encore.")
