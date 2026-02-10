n = int(input())
def valid(n):
    Check = True
    while n > 0:
        if n % 2 != 0:
            Check = False
            break
        n = n // 10
    if Check:
        print("Valid")
    else:
        print("Not valid")
valid(n)