import re
t = input()
n = re.findall(r"\w+", t)
print(len(n))