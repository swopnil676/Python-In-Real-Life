from faker import Faker
fake = Faker()

print(f"Name: {fake.name()}")
print(f"Email: {fake.email()}")
print(f"Address: {fake.address()}")
print(f"Phone: {fake.phone_number()}")