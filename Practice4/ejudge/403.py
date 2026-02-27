n = int(input())
def e_num(n):
    for i in range(0, n + 1):
        if i % 4 == 0 and i % 3 == 0:
            yield i
first = True
for i in e_num(n):
    if first:
        print(i, end = "")
        first = False
    else:
        print(" " + str(i), end = "")