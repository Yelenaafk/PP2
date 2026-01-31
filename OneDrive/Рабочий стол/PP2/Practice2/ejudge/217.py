n = int(input())
count = {}
for _ in range(n):
    number = input().strip()
    count[number] = count.get(number, 0) + 1
answer = 0
for i in count.values():
    if i == 3:
        answer += 1
print(answer)