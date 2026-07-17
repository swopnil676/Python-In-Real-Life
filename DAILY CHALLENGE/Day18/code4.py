# Question 1
data = {
    "name": "Anshul",
    "skills": ["Python", "SQL"],
    "age": 20
}
result = data["skills"][0]
print(result)



# Question 2
data = {
    "name": "Anshul",
    "skills": {
        "language": ["Python", "SQL"],
        "tools": ["Pandas", "Excel"]
    }
}

result = data["skills"]["tools"][0]
print(result)