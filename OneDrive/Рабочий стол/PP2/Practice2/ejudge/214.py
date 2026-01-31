n = int(input())
a = list(map(int, input().split()))
freq = {}
for x in a:
    freq[x] = freq.get(x, 0) + 1#looks for x in a dictionary and if not present returns 0
best = a[0]
for x in freq:
    if freq[x] > freq[best] or (freq[x] == freq[best] and x < best):
        best = x
print(best)