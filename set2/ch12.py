import os
from Crypto.Cipher import *

key = os.urandom(16)
unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode("base64")

def AES_EBC_encrypt(plaintext):
	plaintext = pkcs7(plaintext)
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(plaintext)

def pkcs7(plaintext):
	number = 16-len(plaintext)%16
	paddedtext = plaintext+chr(number)*number
	return paddedtext

def block_size():
	ciphertext = AES_EBC_encrypt(unknown_string)
	val = len(ciphertext)
	for i in range(1,256):
		ciphertext = AES_EBC_encrypt("a"*i+unknown_string)
		if len(ciphertext) > val:
			break
	return len(ciphertext)-val

def detect_ECB(blocksize):
	ciphertext = AES_EBC_encrypt("a"*2*blocksize+unknown_string)
	if ciphertext[:16] == ciphertext[16:32]:
		return True
	return False

def find_unknown_string():
	blocksize = block_size()
	if detect_ECB(blocksize):
		flag = ""
		for i in range(1,9*blocksize+1):
			for j in range(256):
				ciphertext = AES_EBC_encrypt("a"*(9*blocksize-i)+flag+chr(j)+"a"*(9*blocksize-i)+unknown_string)
				if ciphertext[:16*9] == ciphertext[16*9:32*9]:
					break
			flag += chr(j)
	return flag

print find_unknown_string()