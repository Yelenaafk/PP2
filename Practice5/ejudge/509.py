import re
t = input()
n = re.findall(r"\b\w{3}\b", t)
print(len(n))