def StringRotation1(s1,s2):   
    master = s1 + s1
    
    for i in range(len(master)):
        if i + len(s2) > len(master):
            return False
        
        for j in range(len(s2)):
            if master[i+j] == s2[j]:
                if j == len(s2)-1:
                    return True
            else:
                break
"Using slicing"
def StringRotation2(s1,s2):
    master = s1+s1
    for i in range(len(master)):
        if master[i:i+len(s2)] == s2:
            return True
    return False

"Using in"
def StringRotation3(s1,s2):
    master = s1 + s1
    if s2 in master:
        return True
    return False

"Using find (Note: returns index where found if true and -1 if not found. Keep in mind!"
def StringRotation4(s1,s2):
    master=s1+s1
    if master.find(s2) != -1:
        return True
    return False

print(StringRotation1("erbottlewat", "waterbottle"))
