import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# looping through dictionary
for (key, value) in student_dict.items():
    print(key, ":", value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# looping through dataframe
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
