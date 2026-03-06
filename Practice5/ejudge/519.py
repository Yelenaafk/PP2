import re
t = input()
p = re.compile(r"\b\w+\b")
n = p.findall(t)
print(len(n))