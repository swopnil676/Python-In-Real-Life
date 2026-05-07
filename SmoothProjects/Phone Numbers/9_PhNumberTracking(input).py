import phonenumbers
from phonenumbers import geocoder, carrier

number_input = input("Enter phone number with country code (e.g. +919876543210): ")

try:
    number = phonenumbers.parse(number_input, None)

    if phonenumbers.is_valid_number(number):
        region   = geocoder.description_for_number(number, "en")
        network  = carrier.name_for_number(number, "en")
        valid    = "✅ Valid"
    else:
        region  = "Unknown"
        network = "Unknown"
        valid   = "❌ Invalid"

    print("\n--- Phone Number Info ---")
    print(f"Number  : {number_input}")
    print(f"Status  : {valid}")
    print(f"Region  : {region}")
    print(f"Carrier : {network}")

except Exception as e:
    print(f"Error: {e} — Make sure to include country code like +91, +1 etc.")