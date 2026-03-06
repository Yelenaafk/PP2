import re
t = "hello_world_python"
r = re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), t)
print(r)