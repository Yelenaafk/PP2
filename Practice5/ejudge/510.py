import re
t = input()
if re.search(r"cat|dog", t):
    print("Yes")
else:
    print("No")