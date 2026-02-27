import json
s = json.loads(input())
p = json.loads(input())
def apply_p(s, p):
    for key, value in p.items():
        if value is None:
            s.pop(key, None)
        elif key in s and isinstance(s[key], dict) and isinstance(value, dict):
            apply_p(s[key], value)
        else:
            s[key] = value
    return s
print(json.dumps(apply_p(s, p), separators = (',', ':'), sort_keys = True))