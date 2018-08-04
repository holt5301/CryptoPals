import string
from pprint import pprint

def xorSingleChar(inputBytes, character):
    outputBytes = bytearray(len(inputBytes))
    for i in range(len(outputBytes)):
        outputBytes[i] = inputBytes[i] ^ character

    plaintext = outputBytes.decode('utf8', errors='ignore')
    numLets = sum([plaintext.count(letter) for letter in string.ascii_letters + ' '])
    return numLets

def xorAsciiChars(inputBytes):
    results = {}
    for char in range(255):
        numLets = xorSingleChar(inputBytes, char)
        results[char] = numLets
    return results

def main():
    inputHexStr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    inputBytes = bytes.fromhex(inputHexStr)
    print(inputBytes)
    res = xorAsciiChars(inputBytes).items()
    pprint(max(res, key=lambda x: x[1]))

if __name__ == '__main__':
    main()