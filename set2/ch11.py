import os
from Crypto.Cipher import *
from random import *

def AES_ECB_encrypt(plaintext):
	aes = AES.new(random_key(), AES.MODE_ECB)
	return aes.encrypt(plaintext)

def AES_CBC_encrypt(plaintext):
	aes = AES.new(random_key(), AES.MODE_CBC, random_IV())
	return aes.encrypt(plaintext)

def random_key():
	key = os.urandom(16)
	return key

def random_IV():
	IV = os.urandom(16)
	return IV

def random_bytes():
	number = randint(5,10)
	randomBytes = os.urandom(number)
	return randomBytes

def pkcs7(plaintext):
	number = 16-len(plaintext)%16
	paddedtext = plaintext+chr(number)*number
	return paddedtext

def encryption_oracle(plaintext):
	plaintext = random_bytes()+plaintext+random_bytes()
	plaintext = pkcs7(plaintext)*5
	if randint(0,1):
		ciphertext = AES_ECB_encrypt(plaintext)
	else:
		ciphertext = AES_CBC_encrypt(plaintext)
	return ciphertext

def detect_ECB_or_CBC(plaintext):
	ciphertext = encryption_oracle(plaintext)
	ciphertext = [ciphertext[i:i+16] for i in range(0,len(ciphertext),16)]
	if len(ciphertext) == len(set(ciphertext)):
		print "Encrypted with cbc mode of operation"
	else:
		print "Encrypted with ecb mode of operation"

detect_ECB_or_CBC(raw_input("Enter your text : "))