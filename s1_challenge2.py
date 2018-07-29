import base64

print("Hello world")
print("What about this?")

inStr = '1c0111001f010100061a024b53535009181c'
xorStr = '686974207468652062756c6c277320657965'

inputBin = bytearray.fromhex(inStr)
xorBin = bytearray.fromhex(xorStr)

finalArray = bytearray(len(xorBin))

for i in range(len(xorBin)):
    finalArray[i] = inputBin[i] ^ xorBin[i]

print(finalArray.hex())

answer = '746865206b696420646f6e277420706c6179'

print("Correct answer?: {}".format(True if answer == finalArray.hex() else False))
