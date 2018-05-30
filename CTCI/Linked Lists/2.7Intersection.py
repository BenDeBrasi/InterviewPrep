from LinkedList import *

#Recurse through both losts till end. Then on way back keep checking if nodes are equal. First time they are not equal, but .next nodes are that is intersection. If no nodes are ever equal then return None. Also, needs special case if whole lists are equal which can be dealt with be checking if first two nodes are same before the recursion.
def rec_intersect(LL1, LL2):
    print(LL1.head.data,LL2.head.data)

    if LL1 == None and LL2 == None:
        return None

    elif LL1 == None:
        res = intersect(LL1, LinkedList(LL2.head.next))

    elif LL2 == None:
        res = intersect(LinkedList(LL1.head.next), LL2)

    else: 
        res = intersect(LinkedList(LL1.head.next), LinkedList(LL2.head.next))

    if res != None:
        return res
    
    if LL1.head == LL2.head:
        return None
    
    else:
        if LL1.head.next == LL2.head.next and LL1.head.next != None:
            return LL1.head.next

    return None

def intersect1(LL1,LL2):
    if LL1.head == LL2.head:
        return LL1.head
    
    return rec_intersect(LL1,LL2)

#Two pointer approach. Use fact that if there is an intersection it will have to be from min(LL1.size, LL2.size) to end of list. Adjust pointers if lengths are different. Then, iterate through lists checking if node ids are the same. If two nodes are the same that is intersection point so return that node. Otherwise, return None when end of lists are reached.
def intersect(LL1, LL2):
    if LL1 == None or LL2 == None:
        return None
    
    tmp1 = LL1.head
    tmp2 = LL2.head

    if LL1.size > LL2.size:
        tmp1 = catch_up(LL1, LL2)
    elif LL2.size > LL1.size:
        tmp2 = catch_up(LL2, LL1)

    while id(tmp1) != id(tmp2):
        tmp1 = tmp1.next
        tmp2 = tmp2.next

    return tmp1

def catch_up(LL1,LL2):
    tmp = LL1.head
    for i in range(LL1.size - LL2.size):
        tmp = tmp.next
    return tmp


LL1 = LinkedList()
LL2 = LinkedList()
for i in range(20):
    LL1.append(Node(i))
    LL2.append(Node(i))
    if i >= 5:
        LL1.append(Node(i))
        LL2.append(LL1.tail)

print(intersect1(LL1,LL2).data)
