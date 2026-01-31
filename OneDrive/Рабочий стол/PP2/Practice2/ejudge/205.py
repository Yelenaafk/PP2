n = int(input())
base = 2
for i in range(10**8):
    if base ** i == n:
        print("YES")
        break
    elif base ** i > n:
        print("NO")
        break
    else:
        continue