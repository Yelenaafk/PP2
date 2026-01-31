x = int(input())
i = 2
prime = True
while i < x:
    if x % i == 0:
        prime = False
        break
    i += 1
if prime == True:
    print("Yes")
else:
    print("No")