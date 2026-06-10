original = {
    "user": "Sarah",
    "skills": ["Python", "SQL"]
}

copied = original.copy()

copied["user"] = "David"
copied["skills"].append("Docker")

print(original)
print(copied)