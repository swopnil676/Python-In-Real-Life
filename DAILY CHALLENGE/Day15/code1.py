# super() - What Happens If You Skip It in Inheritance
# super() is a built-in Python function used in inheritance
# to access methods and constructors from the parent class.
# It allows child classes to reuse parent code,
# extend functionality, and avoid duplicate logic.
# Without super(), parent variables and methods
# may not initialize properly.

# Python Syntax

# Parent Constructor
class Parent:

    def __init__(self):
        print("Parent")
        
# Child using super()
class Child(Parent):

    def __init__(self):
        super().__init__()


# Example
class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        super().display()
        print("Salary:", self.salary)


emp = Employee("Mike", 80000)

emp.display()

# Output
# Name: Mike
# Salary: 80000