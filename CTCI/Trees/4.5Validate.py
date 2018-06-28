def Validate(T):
    return V(T, minn = T.data, maxx = T.data)

def V(T, minn, maxx):
    if T == None:
        return True
    if T.data < maxx or T.data >= minn:
        return V(T.left, minn, T.data) and V(T.right, T.data, maxx)
    else:
        return False
