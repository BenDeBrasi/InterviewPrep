#Array ascii method no bit vector (original way I coded it).
def isUnique1(st):
	if len(st) > 128:
		return False
		
	list = [0] * 128
	
	for c in st:
		list[ord(c)]+=1
		if list[ord(c)] > 1:
			return False
	
	return True
	
#Sort method
def isUnique2(st):
	st = sorted(st)
	for i in range(1, len(st)):
		if st[i] == st[i-1]:
			return False
	return True

from bitarray import bitarray

#Bitvector ascii method.
def isUnique3(st):
    if len(st) > 128:
        return False
    bitarr = bitarray(128)
    for c in st:
        if bitarr[ord(c)] == True:
            return False
        else:
            bitarr[ord(c)] = True
    return True


print(isUnique3("hh"))	
