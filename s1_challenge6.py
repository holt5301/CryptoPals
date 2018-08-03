import bitstring
import base64
from pprint import pprint

def calcHammingD(bytes1, bytes2):
    res = bytearray(len(bytes1))
    if(len(bytes1) != len(bytes2)):
        print("Not the same length")
        return None
    for i in range(len(bytes1)):
        res[i] = bytes1[i] ^ bytes2[i]
    
    return bitstring.Bits(res).count(1)

def estimateKeyLength(byteData):
    keyLenRes = []
    for keySize in range(2, 41):
        # two consecutive blocks of length equal to the keylength are compared for hamming dist
        # A small hamming distance between two blocks indicates that it's likely the correct length since it's
        # assumed that the plaintext was characters with meaning and not a random distribution of bytes.
        compData1 = byteData[:keySize]
        compData2 = byteData[keySize:2*keySize]

        keyLenRes.append((keySize, calcHammingD(compData1, compData2)/keySize))

    keyLenRes = sorted(keyLenRes, key=lambda x: x[1])[:7] # Only take the 3 lengths with lowest hamming dists
    return keyLenRes

def segmenter(originalList, chunkSize):
    for i in range(0, len(originalList), chunkSize):
        yield originalList[i:i + chunkSize]

with open('6.txt') as f:
    rawData = f.read().replace('\n', '')

byteData = base64.b64decode(rawData)

# Attempting to calculate full key length in bytes
keyLenEsts = estimateKeyLength(byteData) # Only take the 3 lengths with lowest hamming dists

# Need to separate the blocks into sections the same length as the key
cipherBlocks = []
for block in segmenter(list(byteData), keyLenEsts[0][0]):
    cipherBlocks.append(block)

# drop the last segment so that zip functions 
cipherBlocks = cipherBlocks[:-1]

# Collect all first bytes from each block, all second bytes ... etc through the key length byte from each block
cipherTransposed = list(zip(*cipherBlocks))

print(cipherBlocks[:5])
print(list(cipherTransposed)[:5][0])
