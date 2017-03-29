import os
from Crypto.Cipher import *
from random import randint

key = os.urandom(16)
unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode("base64")
random_prefix = os.urandom(randint(4,12))

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

def find_random_prefix_length(blocksize, block_bytes):
	ciphertext = AES_EBC_encrypt(random_prefix+""+unknown_string)
	val = len(ciphertext)
	for i in range(1,256):
		ciphertext = AES_EBC_encrypt(random_prefix+"a"*i+unknown_string)
		ciphertext = ciphertext[blocksize*block_bytes:]
		if ciphertext[16:32] == ciphertext[32:48]:
			break
	return 48-i

def number_of_random_prefix_blocks():
	ciphertext = AES_EBC_encrypt(random_prefix+"a"*48+unknown_string)
	for i in range(0,len(ciphertext)-16,16):
		if ciphertext[i:i+16] == ciphertext[i+16:i+32]:
			break
	return i/16-1

def find_unknown_string():
	blocksize = block_size()
	block_bytes = number_of_random_prefix_blocks()
	prefixsize = find_random_prefix_length(blocksize, block_bytes)
	if detect_ECB(blocksize):
		flag = ""
		for i in range(1,blocksize*9+1):
			for j in range(256):
				ciphertext = AES_EBC_encrypt(random_prefix+"a"*(blocksize-prefixsize)+"a"*(9*blocksize-i)+flag+chr(j)+"a"*(9*blocksize-i)+unknown_string)
				ciphertext = ciphertext[(block_bytes+1)*blocksize:]
				if ciphertext[:blocksize*9] == ciphertext[blocksize*9:2*blocksize*9]:
					break
			flag += chr(j)
	return flag

print find_unknown_string()