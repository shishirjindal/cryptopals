from Crypto.Cipher import *

iv = "\x00"*16
key = "YELLOW SUBMARINE"

def AES_ECB_encrypt(plaintext):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(plaintext)

def AES_ECB_decrypt(ciphertext):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.decrypt(ciphertext)

def xor(s1,s2):
	s3 = "".join([chr(ord(i)^ord(j)) for i,j in zip(s1,s2)])
	return s3

def AES_CBC_decrypt(ciphertext):
	cipher = [ciphertext[i:i+16] for i in range(0,len(ciphertext),16)]
	plaintext = ""
	newiv = iv
	for i in range(len(cipher)):
		intermediate = AES_ECB_decrypt(cipher[i])
		plaintext += xor(intermediate,newiv)
		newiv = cipher[i]
	return plaintext

f = open('10.txt','r').read().replace('\n','')
data = AES_CBC_decrypt(f.decode("base64"))
print data