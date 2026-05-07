import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberFormat


num = phonenumbers.parse("+918482064779")

print("Location:", geocoder.description_for_number(num, "en"))
print("Carrier:", carrier.name_for_number(num, "en"))
print("Timezone:", timezone.time_zones_for_number(num))

        # format of number
print("International:", phonenumbers.format_number(num, PhoneNumberFormat.INTERNATIONAL))
print("National:", phonenumbers.format_number(num, PhoneNumberFormat.NATIONAL))
print("E164:", phonenumbers.format_number(num, PhoneNumberFormat.E164))