m = int(input())
commands = [input().split() for _ in range(m)]
g = 0
n = 0
for cmd, val in commands:
    val = int(val)
    if cmd == "global":
        g += val
    elif cmd == "nonlocal":
        n += val
print(g, n)