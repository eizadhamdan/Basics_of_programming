# reduce function applies a function to an iterable and reduce it to a single cumulative value
# reduce(function, iterable)


import functools


letters = ['E', 'I', 'Z', 'A', 'D']
my_name = functools.reduce(lambda x, y: x + y, letters)
print(my_name)

# calculate factorials
factorials = [1, 2, 3, 4, 5, 6]
factorial = functools.reduce(lambda x, y: x * y, factorials)
print("Factorial of 6 is", factorial)
