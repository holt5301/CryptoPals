import string
from s1_challenge3 import xorAsciiChars
from pprint import pprint

allHexStrs = []

with open('4.txt') as f:
    allHexStrs = f.readlines()

allHexStrs = [line.strip() for line in allHexStrs]

allResults = {}

for i, line in enumerate(allHexStrs):
    res = xorAsciiChars(bytes.fromhex(line)).items()
    maxVal = max(res, key=lambda x: x[1])[1]
    allResults[line] = (i, [word for (word, count) in res if count == maxVal], maxVal)

resList = allResults.items()
pprint(sorted(resList, key=lambda x: x[1][2], reverse=True)[:3])