import base64

inputStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
rawBytes = bytearray.fromhex(inputStr)

answer = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

b64 = base64.b64encode(rawBytes)
print(b64)

print('Correct Answer?: {}'.format(True if answer == b64 else False))