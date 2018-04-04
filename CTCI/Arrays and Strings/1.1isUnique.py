#Array ascii method no bit vector (original way I coded it).
def isUnique1(str):
	if len(str) > 128:
		return False
		
	list = [0] * 128
	
	for c in str:
		list[ord(c)]+=1
		if list[ord(c)] > 1:
			return False
	
	return True
	
#Sort method
def isUnique2(str):
	str.sort()
	for i in xrange(1, len(str)):
		if str[i] == str[i-1]:
			return False
	return True
	
#Bitvector ascii method.
def isUnique3(str):
	if len(str) > 128:
		return False
	