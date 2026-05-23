    # noob
s = "Python1"   #False
only_letters = True
for ch in s:
    if not ch.isalpha():
        only_letters = False
        break
print(only_letters)



    # pro
s = "Python"  # True
print(s.isalpha())
