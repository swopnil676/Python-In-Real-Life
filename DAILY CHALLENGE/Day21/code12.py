# JUNIOR Code
s = "HELLO"
result = ""
for ch in s:
    if "A" <= ch <= "Z":
        result += chr(ord(ch) + 32) # ord(ch) converts a character into its numerical ASCII code (e.g., "A" is 65).
    else:
        result += ch
print(result)


# SENIOR Code
s = "HELLO"
print(s.lower())