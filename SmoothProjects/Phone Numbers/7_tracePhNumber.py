import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def start_phone_tracer(target):
    try:
        print("[+] PhoneTracer v2.1 - OSINT")
        print("[*] Target:", target)
        print("[*] Initialising trace....")

        p = phonenumbers.parse(target, "IN")  # default region (India)

        if phonenumbers.is_valid_number(p):
            location = geocoder.description_for_number(p, "en")
            sim_carrier = carrier.name_for_number(p, "en")
            time_zones = timezone.time_zones_for_number(p)

            print("[+] Location:", location)
            print("[+] Carrier:", sim_carrier)
            print("[+] Timezone:", time_zones)
        else:
            print("[-] Invalid phone number")

        print("[+] Trace complete")

    except Exception as e:
        print("Error:", e)

start_phone_tracer("+919903725334")
