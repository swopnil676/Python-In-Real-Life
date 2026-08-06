word = "PYTHON"
n = len(word)
print(n)

# Top Half
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    letters = " ".join(word[:i])
    print(spaces + letters)

# Bottom Half
for i in range(2, n + 1):
    spaces = " " * (n - i)
    letters = " ".join(word[:i])
    print(spaces + letters)

'''
letters = " ".join(word[:i]) means:

Take the first i letters of the word
            ↓
Separate each letter with a space
            ↓
Store the result in 'letters'
'''

# word = "PYTHON"
#       ↓
# word[:i]
#       ↓
# Take first i characters
#       ↓
# " ".join(...)
#       ↓
# Insert spaces between characters
#       ↓
# Store in letters