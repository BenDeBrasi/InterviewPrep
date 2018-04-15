def CheckPermSort(str1, str2):
    if len(str1) != len(str2):
        return False
		
    sorted(str1)
    sorted(str2)
    
    return str1 == str2
	
def CheckPermArray(str1, str2):
    if len(str1) != len(str2):
        return False
    
    list = [0] * 128
    
    for c in str1:
        list[ord(c)]+=1
    for c in str2:
        list[ord(c)]-=1
    for x in list:
        if x != 0:
            return False
    return True

print(CheckPermArray("helo","hello"))
