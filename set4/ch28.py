import os
import sha1

secret = os.urandom(16)

def pkcs7(plaintext):
	number = 16-len(plaintext)%16
	paddedtext = plaintext+chr(number)*number
	return paddedtext

def auth(mac, message):
	if sha1.Sha1Hash().update(pkcs7(secret+message)).hexdigest() == mac: return True
	return False
