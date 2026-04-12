import phonenumbers
from phonenumbers import is_valid_number

phone_number1 = phonenumbers.parse("+918482064779")

if is_valid_number(phone_number1):
    print("Valid number")
else:
    print("Invalid number")