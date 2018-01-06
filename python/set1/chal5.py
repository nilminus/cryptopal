from utils import *
import math

text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

# Just enough length to overcome the "text" length
# This will be multiplied with the actual key
keylen = int(math.ceil(float(len(text)) / len(key)))
keyarray = bytearray(key * keylen )

cipher = bytes(xor(bytearray(text), keyarray))

print cipher.encode("hex")
