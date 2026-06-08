s = "coding"
rev = ""

for ch in s:
    if ch in "aeiou":
        rev = ch + rev
    else:
        rev = rev + ch

print(rev)


    # Key Idea
# Vowel      → Add at FRONT
# Consonant  → Add at END

    # For "coding":

# Vowels      : o, i  → becomes "io"
# Consonants  : c,d,n,g → remains "cdng"

# Final = "io" + "cdng"
#       = "iocdng"