def PalinPermVector(String):
	
	if len(String) == 0 or len(String) == 1:
		return True
		
	"Replace this with bit vector later"
	alphabet = [0] * 128
	oddFlag = 0
	
	for c in String:
		alphabet[ord(c)]+=1
	
	for i in xrange(len(alphabet)):
		
		if alphabet[i] % 2 != 0:
			if len(String) % 2 == 0:
				return False
			elif len(String) % 2 != 0 and OddFlag = 0:
				oddFlag = 1
			else:
				return False
	return True

def PalinPermSort(String):
	
	if len(String) == 0 or len(String) == 1:
		return True
		
	oddFlag = 0
	currCount = 0
	s = sorted(String)
	
	for i in xrange(1,len(s)):
		
		while(s[i-1] == s[i] and i < len(s)):
			currCount+=1
			i+=1
		
		if currCount % 2 != 0 and len(String) % 2 == 0 or (len(String) %2 != 0 and oddFlag == 1):
			return False
		
		elif currCount % 2 != 0 and len(String) % 2 != 0 and oddFlag == 0:
			oddFlag = 1
		
		currCount = 0

	return True
			
			