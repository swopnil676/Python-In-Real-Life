# By default, when you create a class instance in Python, Python dynamically allocates a hidden dictionary for that object called __dict__. This dictionary stores all of the instance's unique attributes.
# When you define __slots__ = ('name', 'age'), Python skips creating __dict__ entirely. It allocates space specifically for exactly two element references (name and age). This optimization results in:

class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student("Alice", 20)
print(s.name)  # Alice
print(s.age)  # #20
# s.city = "NY" # AttributeError!