import re
t = "a123b axxb a---b"
p = r"a.*b"
print(re.findall(p, t))