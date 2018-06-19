#!/usr/bin/env python
from Crypto.Cipher import AES
obj = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)

# Nice one-liner
ciphertext = ''.join(list(open("7.txt", "r"))).decode('base64')

print obj.decrypt(ciphertext)
