# zip(*iterables)     aggregate elements from two or more iterables(lists, sets, tuples, etc.)
# and creates a zip object with paired elements stored in tuples for each element in our zip object


first_names = ["John", "Dan", "Peter", "Frank"]
last_names = ["Doe", "Brown", "Schmidt", "Walter"]

names = zip(first_names, last_names)

print(names)
names_list = list(names)
# names_dict = dict(names)
# print(names_dict)
# for first_name, last_name in names_dict.items():
#     print(first_name + " " + last_name)
for name in names_list:
    print(name)
