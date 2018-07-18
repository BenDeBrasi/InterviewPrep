from collections import deque

def FCAparent(T,a,b):
    
    heightA = 0
    tmp = a
    
    while tmp != T:
        tmp = tmp.parent
        heightA+=1

    heightB = 0
    tmp = b
    
    while tmp !=T:
        tmp = tmp.parent
        heightB+=1
    
    if heightA >= heightB:
        tmp1 = sameHeight(heightA,a,heightB)
        tmp2 = b
    else:
        tmp1 = sameHeight(heightB,b,heightA)
        tmp2 = a

    while tmp1 != tmp2:
        tmp1 = tmp1.parent
        tmp2 = tmp2.parent

    return tmp1
        

def sameHeight(deeperHeight,deeperNode,higherHeight):
    while deeperHeight != higherHeight:
        deeperNode = deeperNode.parent
        deeperHeight -=1
    return deeperNode

#Solution if no parent pointer
def FCA(T,a,b):
    a = bfs(T.left,a,b)
    b = bfs(T.right,a,b)
    if a and b:
        return T
    elif a:
        return FCA(T.left,a,b)
    else:
        return FCA(T.right,a,b)

def bfs(T,a,b):
    if T == a or T == b:
        return True
    
    Q = deque(T)
    while Q:
        for neigh in T:
            Q.append(neigh)
        
        c = Q.popleft()
        if c == a or c == b:
            return True
    
    return False

