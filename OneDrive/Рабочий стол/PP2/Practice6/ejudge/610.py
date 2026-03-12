n = int(input())
nums = list(map(int, input().split()))
cnt = sum(map(bool, nums))
print(cnt)