from utils import *

max_score = None
plaintext = None
key = None

for line in open("4.txt", "r"):
    line = line.strip()

    b1 = bytearray.fromhex(line)

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1,b2))
        line_score = score(plaintext)

        if line_score > max_score or not max_score:
            max_score = line_score
            result_plaintext = plaintext
            key = chr(i)

print key, result_plaintext
