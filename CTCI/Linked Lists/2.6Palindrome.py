from LinkedList import *
from math import *

#Stack approach.
def palindrome(LL):
    sta = stack()
    tmp = LL.head
    while tmp!=None:
        sta.push(tmp)
        tmp = tmp.next
    tmp = LL.head
    while tmp != None and tmp == sta.peek():
        tmp = tmp.next
        sta.pop()

    if sta.peek() == None and tmp == None:
        return True
    else:
        return False

#Reverse LL approach.
def palindrome1(LL):
    rev = LL
    rev.reverse()
    rev = rev.head 
    tmp = LL.head

    while tmp != None and rev == tmp:
        rev = rev.next
        tmp = tmp.next

    if rev == None and tmp == None:
        return True
    else:
        return False

#Length based approach. Assuming no size() or len() as that would be most complex case.
def palindrome2(LL):
    length = 0
    far = LL.head
    while far != None:
        far = far.next
        length += 1

    length = ceil(length/2)
    far = LL.head
    for i in range(length):
        far = far.next
    near = LL.head
    while far != None and near == far:
        near = near.next
        far = far.next

    if far == None:
        return True
    else:
        return False

LL = LinkedList()
LL.append(Node('a'))
LL.append(Node('b'))
LL.append(Node('a'))
print(palindrome1(LL))
