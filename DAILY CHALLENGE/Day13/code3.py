# I found a bug in python
# Look:

print(hash(1))
# This should print 1...

# Ok...
# But then why...
print(hash(-1))


# More examples
print(hash(0))    # 0
print(hash(1))    # 1
print(hash(2))    # 2
print(hash(-2))   # -2
print(hash(-1))   # -2