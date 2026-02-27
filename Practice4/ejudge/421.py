import importlib
n = int(input())
for _ in range(n):
    mp, an = input().split()
    try:
        module = importlib.import_module(mp)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(module, an):
        print("ATTRIBUTE_NOT_FOUND")
    else:
        attr = getattr(module, an)
        if callable(attr):
            print("CALLABLE")
        else:
            print("VALUE")