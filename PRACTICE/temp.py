import time
import hmac
import hashlib
import struct
import base64

email = "ammarozair02@gmail.com"
secret = email + "HENNGECHALLENGE004"

counter = struct.pack(">Q", int(time.time()) // 30)

hmac_hash = hmac.new(
    secret.encode(),
    counter,
    hashlib.sha512
).digest()

offset = hmac_hash[-1] & 0x0F

code = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7fffffff
code %= 10**10

print(str(code).zfill(10))