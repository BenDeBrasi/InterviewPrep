def StringCompression(s):
    
    if len(s) == 0 or len(s) == 1:
        return s

    compressedString = ""
    
    i = 0
    while i < len(s):
        currLetter = s[i]
        currLetterCount = 0
        
        while i < len(s) and currLetter == s[i]:
            currLetterCount +=1
            i+=1
        
        if currLetterCount > 2:
            compressedString += currLetter
            compressedString += str(currLetterCount)
        else:
            if currLetterCount == 2:
                compressedString += currLetter
            compressedString += currLetter

    if len(compressedString) < len(s):
        return compressedString
    else:
        return s

print(StringCompression("helllllllllllo"))
