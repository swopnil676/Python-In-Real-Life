import phonenumbers
from phonenumbers import region_code_for_number

phone_number1 = phonenumbers.parse("+918482064779")

print("Region Code:", region_code_for_number(phone_number1))
print("Country Code:", phone_number1.country_code)
print("National Number:", phone_number1.national_number)