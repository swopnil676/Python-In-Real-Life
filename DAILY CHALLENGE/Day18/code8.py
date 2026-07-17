# noob
s = "programming"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in s:
    for v in vowels:
        if char == v:
            count = count + 1
            break

print("Number of vowels:", count)


# pro
s = "programming"
vowels = 'aeiou'
print("Number of vowels:", sum(1 for c in s if c in vowels))