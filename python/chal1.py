import codecs
import binascii
import base64

hexed = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
toproduce = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

binari = bytes.fromhex(hexed)

# These are all equiavalent
result = codecs.encode(binari, 'base64').rstrip()
result = binascii.b2a_base64(binari).rstrip()
result = base64.b64encode(binari)

# Remember to decode bytes to get str
if result.decode() == toproduce:
    print("Success")
else:
    print("Failure")
