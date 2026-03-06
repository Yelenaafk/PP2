import re
t = input()
if re.match(r'^[A-Za-z].*[0-9]$', t):
    print("Yes")
else:
    print("No")