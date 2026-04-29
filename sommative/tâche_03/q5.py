# Question 5
eleves = [
    {"nom": "Ava",   "niveau": 12, "activites": ["programmation", "robotique", "mathématiques"]},
    {"nom": "Liam",  "niveau": 11, "activites": ["robotique", "dessin"]},
    {"nom": "Sofia", "niveau": 12, "activites": ["programmation", "mathématiques", "musique", "robotique"]},
    {"nom": "Noah",  "niveau": 10, "activites": ["dessin", "musique"]}
]

for e in eleves:
    print(e["nom"])

print("12e année:", [e["nom"] for e in eleves if e["niveau"] == 12])

toutes = set()
for e in eleves:
    toutes.update(e["activites"])
print("Activités:", toutes)

top = max(eleves, key=lambda e: len(e["activites"]))
print("Plus actif:", top["nom"])

print("En robotique:", sum(1 for e in eleves if "robotique" in e["activites"]))
