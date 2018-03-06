import time

#Create list size of alphabet (ascii values) assumes  with each index representing a letter and initial values at 0. Increment per letter found. If at any point an index is greater than 1 return False. Else return True.

def isUnique1(String):
    
    alphabet = [0] * 128
    
    for c in String:    
        alphabet[ord(c)] +=1
        
        if alphabet[ord(c)] > 1:
            return False
    
    return True

#Similar to above, but uses built in dictionary. Time O(n) Space O(n)
def isUnique2(String):
    
    dictionary = {}
    for c in String:
        #How long does this operation take
        if c in dictonary:
            return False
        else:
            dictionary.update({c:1})
    return True

#Sorted and compare each index to prev. Time: O(nlogn) Space: O(0)
def isUnique3(String):
    #Not sure what happens if xrange(1,1) or xrange(1,0). Will test with time tests.
    if len(String) == 1 or len(String) == 0:
        return True

    sortedString = sorted(String)
    for i in xrange(1,sortedString):
        if sortedString[i-1] == sortedString[i]:
            return False
    return True

#No sort and no extra space. Compare each ele to each other. Time: O(n^2) Space: O(0)
def isUnique4(String):
    for c in String:
        for c2 in String:
            if c == c2:
                return False
    return True

start = time.clock()
print(isUnique1("Helo"))
end = time.clock()
print(end-start)
