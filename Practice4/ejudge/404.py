a, b = map(int, input().split())
def squares(a, b):
    for i in range(a, b + 1):
            yield i ** 2
for i in squares(a, b):
    print(i)