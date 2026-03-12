n = int(input())
nums = list(map(int, input().split()))
sqrs = map(lambda x: x**2, nums)
sum = 0
for i in  nums:
    sum += i**2
print(sum)