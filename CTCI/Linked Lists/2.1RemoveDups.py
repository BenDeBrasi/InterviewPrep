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


LL = LinkedList()
for i in range(10):
    LL.prepend(Node(i))

tmp = LL.head
while tmp != None:
    print(tmp.data)
    tmp = tmp.next

RevDupNoBuf(LL)

print("-----")
print("Testing iter")
for i in LL:
    print(i.data)


print("----")
print(LL.head)

tmp = LL.head
while tmp != None:
    print(tmp.data)
    tmp = tmp.next
