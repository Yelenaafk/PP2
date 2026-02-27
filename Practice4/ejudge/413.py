import json
def qengine(data, query):
    cur = data
    parts = query.split('.')
    for part in parts:
        while '[' in part:
            key, rest = part.split('[', 1)
            if key:
                if isinstance(cur, dict) and key in cur:
                    cur = cur[key]
                else:
                    return "NOT_FOUND"
            index_str, rest = rest.split(']', 1)
            try:
                index = int(index_str)
            except:
                return "NOT_FOUND"
            if isinstance(cur, list) and 0 <= index < len(cur):
                cur = cur[index]
            else:
                return "NOT_FOUND"
            part = rest
        if part:
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return "NOT_FOUND"
    return json.dumps(cur, separators=(',', ':'))
data = json.loads(input())
q = int(input())
for _ in range(q):
    query = input().strip()
    print(qengine(data, query))