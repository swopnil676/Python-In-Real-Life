print(dir(frozenset))

print("\n")

methods = []
for m in dir(frozenset):
    if not m.startswith("__"):
        methods.append(m)

print(methods)
