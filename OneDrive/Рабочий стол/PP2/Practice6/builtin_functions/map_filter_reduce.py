from functools import reduce
numbers = [1, 2, 3, 4, 5]
#map: multiply each element by 2
mapped = list(map(lambda x: x * 2, numbers))
print(mapped)
#filter: keep only even numbers
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)
#reduce: product of all elements
product = reduce(lambda x, y: x * y, numbers)
print(product)