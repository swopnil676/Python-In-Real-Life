# @staticmethod vs @classmethod
# @staticmethod vs @classmethod are method decorator used inside classes.
# they controlled how method interact with class and object
class MyClass:

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass


# Example

class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

    @staticmethod
    def is_high_salary(salary):
        return salary > 100000


emp = Employee.from_string("Rob-120000")

print(emp.name)
print(emp.salary)
print(Employee.is_high_salary(emp.salary))
