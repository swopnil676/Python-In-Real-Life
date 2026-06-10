# **kwargs in python

def anyFunc(**names):
    print(
        f"His first name is "
        f"{names['firstName']}\n"
        f"and his last name is "
        f"{names['lastName']}\n"
    )

anyFunc(
    firstName = "Dani",
    lastName = "Daniels"
)