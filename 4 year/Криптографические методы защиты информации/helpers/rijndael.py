# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import binascii

data = b"This is the message for IFMO...."


key = b"Sixteen byte key"
cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(data)
print(binascii.hexlify(ciphertext))

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
