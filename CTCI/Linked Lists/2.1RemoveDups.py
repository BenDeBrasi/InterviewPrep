from LinkedList import *
"""
import importlib

importlib.import_module("LinkedList")
"""
def RevDupBuf(LL):    

    dic = {}
    tmp = LL.head
    ele = LL.head
    
    while ele != None:
        if ele.data in dic:
            tmp.next = ele.next
        else:
            dic[ele.data]= True
            tmp = ele 
        ele = ele.next
    return LL

def RevDupNoBuf(LL):
    ele = LL.head

    while ele != None:
        curr = ele.next
        prev = ele

        while curr != None:

            if ele.data == curr.data:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        ele = ele.next
    return LL

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(5)
LL = LinkedList(a)
LL.add(b)
LL.add(c)
LL.add(d)

tmp = LL.head
while tmp != None:
    print(tmp.data)
    tmp = tmp.next

RevDupNoBuf(LL)

print("----")

tmp = LL.head
while tmp != None:
    print(tmp.data)
    tmp = tmp.next
