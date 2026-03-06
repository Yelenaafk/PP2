import re
s = input()
p = input()
m = re.findall(p, s)
print(len(m))