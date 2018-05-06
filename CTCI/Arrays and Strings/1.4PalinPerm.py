from BitVector import BitVector

def PalinPermVector(String):
    
    if len(String) == 0 or len(String) == 1:
        return True
    
    alphabet = BitVector(intVal=0,size=128)
    oddFlag = 0
    
    for c in String:
        print(ord(c))
        if alphabet[ord(c)] == 1:
            alphabet[ord(c)]=0
        else:
            alphabet[ord(c)]=1
            
    for i in range(len(alphabet)):
        if alphabet[i] % 2 != 0:
            if len(String) % 2 == 0:
                return False
            elif len(String) % 2 != 0 and oddFlag == 0:
                oddFlag = 1
            else:
                return False
    return True

def PalinPermSort(String):
    
    if len(String) >= 0 and len(String) <= 2:
        return True
    
    oddFlag = 0
    s = sorted(String)
    i = 0    
    
    while i < len(s):
        
        currCount = 0
        currChar = s[i]

        while(i < len(s) and currChar == s[i]):
            currCount+=1
            i+=1
            
        if (currCount % 2 != 0 and len(String) % 2 == 0) or (len(String) %2 != 0 and oddFlag == 1 and currCount % 2 != 0):
            return False
		
        elif currCount % 2 != 0 and len(String) % 2 != 0 and oddFlag == 0:
            oddFlag = 1

    return True
			
print(PalinPermSort("aabbcc"))
