import phonenumbers
from phonenumbers import geocoder, carrier

number = phonenumbers.parse("+918482064779", None)

# Validate
print(phonenumbers.is_valid_number(number))

# Region (country only)
print(geocoder.description_for_number(number, "en"))

# Carrier
print(carrier.name_for_number(number, "en"))