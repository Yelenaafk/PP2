from functools import reduce
numbers = [1, 2, 3, 4, 5]
#length of the list
print(len(numbers))
#sum of elements
print(sum(numbers))
#minimum and maximum values
print(min(numbers))
print(max(numbers))
#enumerate: index and value pairs
for index, value in enumerate(numbers):
    print(index, value)
#zip: combine two lists
letters = ['a', 'b', 'c', 'd', 'e']
zipped = list(zip(numbers, letters))
print(zipped)
#sorted list (descending)
print(sorted(numbers, reverse=True))
#type conversion functions
print(int("10"))
print(float("3.14"))
print(str(100))
print(list((1, 2, 3)))
print(tuple([4, 5, 6]))
print(set([1, 2, 2, 3]))