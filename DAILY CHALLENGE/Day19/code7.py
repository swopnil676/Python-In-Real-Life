names = ["Rahul", "Neha", "Aman"]
scores = [85, 92, 78]
ages = [21, 22, 20]

# Method 1
for i in range(len(names)):
    print((names[i], scores[i], ages[i]))


# Method 2
p = list(zip(names, scores, ages))
print(p)
