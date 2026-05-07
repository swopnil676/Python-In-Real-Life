import phonenumbers
from phonenumbers import number_type, PhoneNumberType

num = phonenumbers.parse("+918482064779")
# num = phonenumbers.parse("+14155550132")

t = number_type(num)

if t == PhoneNumberType.MOBILE:
    print("Mobile Number")
elif t == PhoneNumberType.FIXED_LINE:
    print("Landline")
elif t == PhoneNumberType.VOIP:
    print("Internet Number")
else:
    print("Other type")