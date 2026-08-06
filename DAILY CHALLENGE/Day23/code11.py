# First Non-Repeating Character in python

word = "aabbccddee"

for ch in word:
    if word.count(ch) == 1:
        print(ch)
        break
else:
    print("No non-repeating character found")
    # The else runs ONLY if the loop finishes without break




# Using Counter

from collections import Counter

word = "aabbcde"

freq = Counter(word) # {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1}

for ch in word:
    if freq[ch] == 1:
        print(ch)
        break
else:
    print("No non-repeating character found")