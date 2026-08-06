# Question 1
student = {"name": "Emily", "age": 22}

# print(student["city"]) # KeyError: 'city'
student = {"name": "Emily", "age": 22}
print(student.get("city", "Not Found"))



# Question 2
student = {
    "name": "Emily",
    "age": 22,
    "city": {
        # "name": "New York"
    }
}

print(student["city"].get("name", "Not Found"))
'''
student
│
├── "name" → "Emily"
├── "age"  → 22
└── "city"
      │
      └── {"name": "New York"}
                │
                └── get("name")
                        │
                        └── "New York"
'''