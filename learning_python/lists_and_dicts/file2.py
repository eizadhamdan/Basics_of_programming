# Dictionary Comprehension

import random


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

temperatures_in_cels = {
    "Monday": 12,
    "Tuesday": 13.6,
    "Wednesday": 10,
    "Thursday": 15,
    "Friday": 20,
    "Saturday": 17.5,
    "Sunday": 18
}
temps_in_fahr = {day: round((1.8 * temp + 32), 2) for (day, temp) in temperatures_in_cels.items()}
print("Temperatures in celsius:", temperatures_in_cels)
print("Temperatures in fahrenheit:", temps_in_fahr)
