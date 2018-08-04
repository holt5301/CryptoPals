import bitstring
import base64
from pprint import pprint
from s1_challenge3 import xorAsciiChars
from itertools import groupby

def segmenter(originalList, chunkSize):
    for i in range(0, len(originalList), chunkSize):
        yield originalList[i:i + chunkSize]

def calcHammingD(bytes1, bytes2):
    res = bytearray(len(bytes1))
    if(len(bytes1) != len(bytes2)):
        print("Not the same length")
        return None
    for i in range(len(bytes1)):
        res[i] = bytes1[i] ^ bytes2[i]

    return bitstring.Bits(res).count(1)

def estimateLikelyKeyLens(byteData, numLens=3):
    keyLenRes = []
    for keySize in range(10, 41):
        # two consecutive blocks of length equal to the keylength are compared for hamming dist
        # A small hamming distance between two blocks indicates that it's likely the correct length since it's
        # assumed that the plaintext was characters with meaning and not a random distribution of bytes.
        hdists = []
        chunks = list(segmenter(byteData, keySize))[:-1] # Chop off last partial chunk
        while len(chunks) >= 2:
            compData1 = chunks.pop(0)
            compData2 = chunks.pop(0)
            hdists.append(calcHammingD(compData1, compData2))

        avg = sum(hdists)/len(hdists)

        keyLenRes.append((keySize, avg/keySize))

    keyLenRes = sorted(keyLenRes, key=lambda x: x[1])[:numLens] # Sort by hammingdist index then take lowest "numLens" items
    #print("Keylengths are: {}".format(keyLenRes))
    return [lenIndxPair[0] for lenIndxPair in keyLenRes]

with open('6.txt') as f:
    rawData = f.read().replace('\n', '')

cipherData = bytes(base64.b64decode(rawData))

# Attempting to calculate full key length in bytes
keyLenEsts = estimateLikelyKeyLens(cipherData, numLens=1) # Only take the 7 lengths with lowest hamming dists
print(keyLenEsts)

for currKeyLen in keyLenEsts:
    # Need to separate the blocks into sections the same length as the key
    # i.e. "aklsjn;jn" becomes "akl","sjn",";jn" for a key length of 3
    cipherBlocks = []
    for block in segmenter(list(cipherData), currKeyLen):
        cipherBlocks.append(block)

    # drop the last segment so that zip functions
    cipherBlocks = cipherBlocks[:-1]
    # Collect all first bytes from each block, all second bytes ... etc through the key length byte from each block
    cipherTransposed = list(zip(*cipherBlocks))

    keyChars = []
    # For each block which corresponds to a byte alignment process
    for currCiphTrans in cipherTransposed:
        # Get results for character and it's corresponding number of letters in output
        resultDict = xorAsciiChars(currCiphTrans)
        # Get the character which had the highest number of letters
        likelyChar = max(resultDict.items(), key=lambda x: x[1])[0]
        keyChars.append(likelyChar)

    key = bytearray([char for char in keyChars])

    pprint("Key is: {}".format(key.decode('utf8')))

    testCipherData = bytearray(len(cipherData))
    for i, byte in enumerate(cipherData):
        #print("Applying key byte: {}".format(key[i % len(key)]))
        testCipherData[i] = cipherData[i] ^ key[i % len(key)]

    print("Deciphered text is: {}".format(testCipherData.decode('utf8')))
