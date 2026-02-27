import json
a = json.loads(input())
b = json.loads(input())
def deep_diff(a, b, path = ""):
    diff = []
    keys = set(a.keys()) | set(b.keys())
    for key in keys:
        fp = f"{path}.{key}" if path else key
        av = a.get(key, "<missing>")
        bv = b.get(key, "<missing>")
        if isinstance(av, dict) and isinstance(bv, dict):
            diff.extend(deep_diff(av, bv, fp))
        elif av != bv:
            a_s = json.dumps(av, separators = (',', ':')) if av != "<missing>" else "<missing>"
            b_s = json.dumps(bv, separators = (',', ':')) if bv != "<missing>" else "<missing>"
            diff.append(f"{fp} : {a_s} -> {b_s}")
    return diff
diff = deep_diff(a, b)
if diff:
    for line in sorted(diff):
        print(line)
else:
    print("No differences")