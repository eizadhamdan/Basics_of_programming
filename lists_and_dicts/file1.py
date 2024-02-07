# List Comprehension

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Hamdan"
letters_list = [letter for letter in name]
print(letters_list)

num_list = [num * 2 for num in range(1, 5)]
print(num_list)

mult_of_four_list = [num for num in range(1, 60) if num % 4 == 0]
print(mult_of_four_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

numbers = [pow(num, 2) for num in range(20)]
print(numbers)

even_nums = [num for num in range(30) if num % 2 == 0]
print(even_nums)

# finding intersection of two lists
common_nums = [number for number in even_nums if number in numbers]
print(common_nums)
