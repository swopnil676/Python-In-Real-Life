# Student Grading System
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")

s1 = Student("Niharika", 97)
s1.result()

s2 = Student("Tommy", 34)
s2.result()