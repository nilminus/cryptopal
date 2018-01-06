string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
toproduce = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

decoded = string.decode("hex")
print "Decoded string is: {}".format(decoded)

result = decoded.encode('base64').strip()
print "Base64 string is: {}".format(result)

if result == toproduce:
    print "[+] SUCCESS"
else:
    print "[+] FAILURE"
