n = int(input())
attendance = set()
for i in range(n):
    sname = input().strip()
    attendance.add(sname)
print(len(attendance))