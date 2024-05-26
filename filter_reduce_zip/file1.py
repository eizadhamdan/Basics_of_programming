# filter function creates a collection of elements from an iterable for which a function returns True
# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 16),
           ("Joey", 17),
           ("Chandler", 21),
           ("Ross", 20)]

filtered_list = list(filter(lambda data: data[1] >= 18, friends))
print(filtered_list)
