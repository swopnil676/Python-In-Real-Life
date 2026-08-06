# Find the most frequent word in a string

    # Method 1
text = "python spark python kafka spark python"

words = text.split()

freq = {} # use {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(list(freq.items())[0])
print(freq)


    # Method 2
text = "python spark python kafka spark python"

words = text.split()

freq = [] # use []

for word in words:
    found = False

    for i in range(len(freq)):
        if freq[i][0] == word:
            freq[i][1] += 1
            found = True
            break

    if not found:
        freq.append([word, 1])

print(freq[0]) 
print(freq)