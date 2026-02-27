def lim_cyc(l, k):
    for j in range(k):
        for i in range(0, len(l)):
            yield l[i]
l = list(map(str, input().split()))
k = int(input())
for i in lim_cyc(l, k):
    print(str(i) + " ", end = "")