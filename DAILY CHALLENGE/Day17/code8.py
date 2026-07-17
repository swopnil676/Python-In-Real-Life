def greet(**python):
    for key, value in python.items():
        print(f"{key.capitalize()}: {value}")

greet(name="John", 
      age=25, 
      location="New York", 
      hobby="Reading")