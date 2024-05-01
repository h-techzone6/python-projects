import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

#Enter your phone number with country code
number = "+93"
number=ph.parse(number)

print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number,"en"))
print(geocoder.description_for_number(number,"en"))