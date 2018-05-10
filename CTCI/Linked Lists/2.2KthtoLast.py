from LinkedList import *

def kth(LL, k):
    
    later = LL.head
    
    for i in range(k):
        later = later.next
    
    target = LL.head
    while later.next != None:
        target = target.next
        later = later.next

    return target

global count

def kthRec(LL,k):
    if LL.head is None:
        return None

    n = kthRex(LL.head.next,k)
    count += 1 
    
    if count == k:
        return LL.head
    
    return n


print(kthRex())
