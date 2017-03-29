def pkcs(s):
	print "16 byte block padding"
	a = len(s)
	number = 16-a%16
	padding = ("\\x"+bytes(number))*number
	return s+padding

print "Padded text : "+pkcs(raw_input())

