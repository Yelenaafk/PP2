import re
t = input()
if re.match(r"^Hello", t):
    print("Yes")
else:
    print("No")