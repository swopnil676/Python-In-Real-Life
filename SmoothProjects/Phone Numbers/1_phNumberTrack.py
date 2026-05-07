import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+918482064779")

print("\nPhone Numbers Location: ")

location = geocoder.description_for_number(phone_number1,"en")
print(location)

print("Country Code:", phone_number1.country_code)
print("National Number:", phone_number1.national_number)