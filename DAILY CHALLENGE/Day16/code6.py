text = input("Enter a text: ")
for _ in "aeiouAEIOU":
    text = text.replace(_, "")
print(text)


a = 256
b = 256
c = 257
d = 257
print(a is b, c is d)
