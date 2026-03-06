import re
s = input()
p = input()
ep = re.escape(p)
m = re.findall(ep, s)
print(len(m))