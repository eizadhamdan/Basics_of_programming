# map function applies a function to an iterable(list, tuple, etc.)
# map(function, iterable)

# prices are in dollars
store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_rupee = lambda data: (data[0], data[1] * 83.09)

store_rupees = list(map(to_rupee, store))

for item in store_rupees:
    print(item, end="_____")
