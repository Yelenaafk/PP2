n = int(input())
def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
            yield a
            a, b = b, a + b
first = True
for i in fibonacci(n):
    if first:
        print(i, end = "")
        first = False
    else:
        print("," + str(i), end = "")