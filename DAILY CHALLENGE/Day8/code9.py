s = "aabbcdeff"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character is :",ch)
        break