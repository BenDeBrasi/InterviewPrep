def oneAway(str1, str2):
    
    if str1 == str2:
        return True		
    elif not(len(str1) == len(str2) or len(str1)-1 == len(str2) or len(str1)+1 == len(str2)):
        return False
    elif len(str1) < len(str2):
        return compare(str1,str2)
    else:
        return compare(str2,str1)
		
def compare(str1,str2):
    difference = 0
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if difference == 0:
                difference = 1
                if len(str1) < len(str2):
                    i -= 1
            else:
                return False
        i+=1
        j+=1
    return True

print(oneAway("pale","bale"))
