# Repeating XOR
# Secret key is "ICE"

plaintextBytes = bytearray(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
secKey = b'ICE'
answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
print("Start text is: \"{}\"".format(plaintextBytes.decode('utf8')))
print("Secret Key is: {}, length {}".format(secKey, len(secKey)))

for i, byte in enumerate(plaintextBytes):
    plaintextBytes[i] ^= secKey[i % len(secKey)]
    #print("Index {} is byte {} converted to {}".format(i, chr(byte), hex(plaintextBytes[i])))

print(plaintextBytes.hex())
print("Correct answer? {}".format(plaintextBytes.hex() == answer))