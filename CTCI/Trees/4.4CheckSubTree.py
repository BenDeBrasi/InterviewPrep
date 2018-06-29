def CheckSubTree(T):
    if T == None:
        return False
    if abs(gH(T.left) - gH(T.right)) > 1:
        return False
    else:
        return CheckSubTree(T.left) and CheckSubTree(T.right)

def gH(T):
    if T == None:
        return -1

    return max(gH(Tleft) - gH(T.right)) + 1

def CheckTree(T):
    if T == None:
        return False
    if getH(T.left) == sys.maxsize or getH(T.right) == sys.maxsize:
        return False
    else:
        return True

def getH(T):
    if T == None:
        return -1
    
    l = getH(T.left)
    if l == sys.maxsize:
        return l

    r = getH(T.right)
    if r == sys.maxsize:
        return r

    if abs(l-r) > 1:
        return sys.maxsize
    else:
        return max(l,r)+ 1
