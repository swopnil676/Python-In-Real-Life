student = {
    "name": "Shiva",
    "age": 22
}

# print(student["class"]) #==>> KeyError: 'class'
print(student.get("class",0)) #default class = 0 