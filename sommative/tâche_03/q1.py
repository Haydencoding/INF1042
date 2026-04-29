# Question 1
notes = [78, 85, 92, 67, 85, 74]

print(notes)
print(notes[0], notes[-1])
notes.append(88)
notes.remove(85)
print(notes)
print("Total:", sum(notes))
print("Moyenne:", sum(notes) / len(notes))
print("Max:", max(notes), "Min:", min(notes))
