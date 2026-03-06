import re
nameage = input()
match = re.match(r"Name: (.+), Age: (.+)", nameage)
if match:
    x, y = match.groups()
    print(f"{x} {y}")