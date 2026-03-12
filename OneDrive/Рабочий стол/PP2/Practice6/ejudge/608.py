n = int(input())
nums = list(map(int, input().split()))
distsort = sorted(set(nums))
print(*distsort)