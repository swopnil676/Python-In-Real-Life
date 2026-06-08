emails = [
    "john.doe@gmail.com",
    "alice123@yahoo.com",
    "michel_smith@outlook.com",
    "pythonlover@ptotonmail.com",
    "akash_b@gmail.com",
    "dev.user@icloud.com",
    "coderhub@fastmail.com",
    "techworld@hotmail.com",
    "data.science@edu.in",
    "machinelearning@openai.com"
]

usernames = [email.split("@")[0] for email in emails]
print(usernames)