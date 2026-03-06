import re
s = input()
p = input()
r = input()
result = re.sub(re.escape(p), r, s)
print(result)