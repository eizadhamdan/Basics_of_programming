# sorting a list of tuples
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Kramer", "C", 70)]

# by default, they are sorted by the first entry
sorted_students = sorted(students)
print(sorted_students)

# sorting by grades
sorted_students = sorted(students, key=lambda grades: grades[1])
print(sorted_students)

# reverse sorting by marks
students.sort(key=lambda age: age[2], reverse=True)
print(students)
