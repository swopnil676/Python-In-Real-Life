a = [1,2]
b = [3,4]

# noob
merged = a.copy()
for i in b:
    merged.append(i)
print(merged)

# pro
print(a + b)
# or,
a.extend(b)
print(a)