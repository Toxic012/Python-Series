import phonenumbers
from phonenumbers import geocoder 

phonenumbe_1 = phonenumbers.parse("+918019491248")  # Indian number
phonenumbe_2 = phonenumbers.parse("+1(475)351-5353")  # US number

location = geocoder.description_for_number(phonenumbe_1, "en")
lo = geocoder.description_for_number(phonenumbe_2, "en")

print(phonenumbe_1)  # Prints the parsed PhoneNumber object
print(location)      # Should print something like: "Karnataka"
print(lo)            # Should print something like: "Connecticut"
