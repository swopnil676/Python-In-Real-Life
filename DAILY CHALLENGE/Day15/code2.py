# Multiple Inheritance – Which Method Wins in class C(A, B)
# Multiple inheritance means a class inherits
# from more than one parent class.
# Python follows Method Resolution Order (MRO)
# and searches parent classes from left to right.
# It decides which method gets executed
# and how inheritance chains work internally.

# Syntax
class A:
    pass

class B:
    pass

class C(A, B):
    pass


# Example
class Camera:

    def feature(self):
        print("Camera Feature")

class Phone:

    def feature(self):
        print("Phone Feature")

class SmartPhone(Camera, Phone):
    pass

# s = SmartPhone()
# s.feature()
SmartPhone().feature()

print(SmartPhone.mro()) # The .mro() method stands for Method Resolution Order. It shows you the exact lookup path Python has pre-calculated for that class.


# Output
# Camera Feature
# [<class '__main__.SmartPhone'>, <class '__main__.Camera'>, <class '__main__.Phone'>, <class 'object'>]

# Real World Use
# Multiple Inheritance Used In:
# Django class-based views
# Game engines
# GUI frameworks
# Authentication systems