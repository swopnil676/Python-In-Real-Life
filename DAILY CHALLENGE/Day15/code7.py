total = 25
if total >=25 or "vip":
    print("Free shipping")
else:
    print("Pay shipping")



# Pro Type
settings = {
    "theme": "light",
    "lang": "en",
    "alerts": False
}

user_settings = {
    "theme": "dark",
    "alerts": True
}

settings |= user_settings
print(settings)