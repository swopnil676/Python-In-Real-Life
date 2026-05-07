# noob
words = ["Python", "is", "fun"]
sentence = ""
for i,w in enumerate(words):
    sentence += w
    if i<len(words) - 1:
        sentence += " "
print(sentence)


# pro
words = ["Python", "is", "fun"]
print(" ".join(words))
