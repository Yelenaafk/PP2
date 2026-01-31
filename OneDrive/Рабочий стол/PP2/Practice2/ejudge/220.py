import sys
a = {}
arr = sys.stdin.read().splitlines()
n = int(arr[0])
id = 1
for _ in range(n):
    b = arr[id].split()
    id += 1
    if b[0] == "set":
        a[b[1]] = b[2]
    else:
        print(a.get(b[1], f"KE: no key {b[1]} found in the document"))