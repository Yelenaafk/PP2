def twosquare(n):
    for i in range(0, n + 1):
        yield 2 ** i
n = int(input())
for i in twosquare(n):
    print(str(i) + " ", end = "")