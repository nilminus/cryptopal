#!/usr/bin/env python
from utils import *

text = ""
for line in  open("6.txt", "r"):
  text += line.rstrip()

ciphertext = text.decode('base64')

KEYSIZE = keysize_from_ciphertext(ciphertext)[0][0] # Keysize of first (sorted) tuple

# Now transpose the blocks: make a block that is the first byte of every block, 
# and a block that is the second byte of every block, and so on.
block_bytes = [[] for i in range(KEYSIZE)]
for i, byte in enumerate(ciphertext):
  block_bytes[i % KEYSIZE].append(byte)

keys = ''
for block in block_bytes:
  keys += break_single_key_xor(''.join(block))[0]

key = bytearray(keys * len(text))
key = bytearray(keys * (len(text) / (KEYSIZE +1)))
plaintext = bytes(xor(bytearray(ciphertext), key))

print "Encryption key is: {}".format(keys)
print "Encryption key size is: {}".format(KEYSIZE)
# print plaintext
