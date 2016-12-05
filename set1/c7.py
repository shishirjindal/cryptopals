import base64
from Crypto.Cipher import AES

f = base64.b64decode(open("7.txt","r").read())
en = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
data = en.decrypt(f)
print data