    # noob
# s = "education"
s = str(input("Enter any word: "))
vowels = "aeiou"

count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)       

    # pro
s = "education"
# s = str(input("Enter any word: "))
print(sum(
    ch in "aeiou" for ch in s
))