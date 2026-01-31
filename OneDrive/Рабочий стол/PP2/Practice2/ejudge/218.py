n = int(input())
arr = [input().strip() for _ in range(n)]
fp = {}
for i, s in enumerate(arr, start=1):
    if s not in fp:
        fp[s] = i
for s in sorted(fp):
    print(s, fp[s])