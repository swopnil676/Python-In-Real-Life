import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter phone number with country code: ")

num = phonenumbers.parse(number)

print("\n--- Phone Info ---")
print("Valid:", phonenumbers.is_valid_number(num))
print("Location:", geocoder.description_for_number(num, "en"))
print("Carrier:", carrier.name_for_number(num, "en"))
print("Timezone:", timezone.time_zones_for_number(num))