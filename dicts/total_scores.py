students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "John", "score": 70},
    {"name": "Mina", "score": 95}
]
total = 0
for student in students:
    total += student["score"]
    print(total)
average = total / len(students)
print(average)