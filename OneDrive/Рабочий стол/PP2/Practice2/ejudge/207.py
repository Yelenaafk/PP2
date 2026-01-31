n = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
for i in range(n):
    if arr[i] == max_val:
        print(i + 1)