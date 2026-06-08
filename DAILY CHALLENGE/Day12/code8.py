# Question 1
def person(greet, *names):
    for name in names:
        print(greet, name)

person("Hello", "krishna", "dina", "rasid", "amelina")


# Question 2
s = "python can make magic"
print(" ".join(s.split()[::-1]))

# s.split() :- ['python', 'can', 'make', 'magic']
# " ".join(...) :- "magic make can python"