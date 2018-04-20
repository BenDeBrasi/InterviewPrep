def StringCompression(str):
    currLetter = ' '
    currLetterCount = 0
    compressedString = ""
    
    for i in xrange(len(str)):
        currLetter = str[i]
        
        while currLetter = str[i] and i < len(str):
            currLetterCount +=1
            
            compressedString += currLetter
            compressedString += currLetterCount
            
            currLetter = ' '
            currLetterCount = 0
		
    if len(compressedString) < len(str):
        return compressedString
    else:
        return str
