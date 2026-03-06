import re
t = "hello_world test_case Example_text"
p = r"[a-z]+_[a-z]+"
print(re.findall(p, t))