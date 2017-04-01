from Crypto.Cipher import *
from superlib import xor

key = 'YELLOW SUBMARINE'
nonce = "\x00"*8
cipher = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==".decode("base64")

def AES_ECB_encrypt(key, data):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(data)

def AES_CTR(ciphertext, key, nonce):
	keystream = ""
	for i in range(len(ciphertext)/16+1):
		data = nonce + chr(i) + "\x00"*(8-len(chr(i)))
		keystream += AES_ECB_encrypt(key, data)
	return xor(keystream, ciphertext)

print AES_CTR(cipher, key, nonce)
