f = open('8.txt','r')

def is_ECB(s):
	l = [s[x:x+32] for x in range(0,320,32)]
	if len(l)!=len(set(l)): return True
	else: False
 
for s in f:
	if is_ECB(s[:-1]): print s[:-1]