import string

inputHexStr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

inputBytes = bytearray.fromhex(inputHexStr)
outputBytes = bytearray(len(inputBytes))
print(inputBytes)

for char in string.ascii_letters:
    print("Testing character: {}".format(char))
    for i in range(len(outputBytes)):
        outputBytes[i] = inputBytes[i] ^ ord(char)

    plaintext = outputBytes.decode('utf8')
    print(outputBytes)

    numLets = sum(plaintext.count(letter) for letter in string.ascii_letters)

    print("Number of letters: {}".format(numLets))