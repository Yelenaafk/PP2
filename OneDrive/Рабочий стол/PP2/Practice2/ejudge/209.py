n = int(input())
arr = list(map(int, input().split()))
max = max(arr)
min = min(arr)
for i in range(n):
    if arr[i] == max:
        arr[i] = min
    print(arr[i], end = " ")