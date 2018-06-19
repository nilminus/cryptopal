from utils import *

b1 = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
b2 = bytearray.fromhex("686974207468652062756c6c277320657965")

b = bytes(xor(b1, b2))
print b
print b.encode('hex')
