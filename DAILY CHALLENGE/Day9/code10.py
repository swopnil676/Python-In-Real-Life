    # part 1
words = ["jalpaiguri", "government", "engineering", "college"]
text = " ".join(words)
print(text)

    # part 2
char = "jalpaiguri government engineering college"
for word in char.split():
    print(word[0], end="")
print() # for new line


    # part 3
words = ["jalpaiguri", "government", "engineering", "college"]
for ch in words:
    print(ch[0],end="")
    