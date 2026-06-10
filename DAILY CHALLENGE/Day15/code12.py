class Person:
    def __init__(self,name):
        self.name=name

    def say_hello(self):
        print("Hello {} !".format(self.name))
        # .format() Execution: The .format() method takes "Adam" and injects it directly into the curly braces {} placeholder.

adam = Person('Adam')
adam.say_hello()