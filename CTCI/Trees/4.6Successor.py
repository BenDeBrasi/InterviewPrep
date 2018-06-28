def Successor(n):
    
    if n == None:
        return n

    if n.right == None:
        while n.parent.left != n:
            n = n.parent
            if n.parent == None:
                return None
        return n

    else:
        n = n.right
        while n.left != None:
            n = n.left
        return n
