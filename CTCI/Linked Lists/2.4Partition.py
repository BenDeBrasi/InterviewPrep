from LinkedList import *

#Create two linked lists (LL1, LL2) then iterate through list passed in. Each element less than partitioning value.prepend to LL1 and each greater or equal to.prepend to LL2. Then append LL2 to LL1 and return LL1.

def Partition(LL,part):
    LL1 = LinkedList(None)
    LL2 = LinkedList(None)

    tmp = LL.head
    while tmp != None:
        if tmp.data < part:
            LL1.prepend(Node(tmp.data))
        else:
            LL2.prepend(Node(tmp.data))
        tmp = tmp.next

    for j in LL1:
        print("LL1: ", j.data)
    for k in LL2:
        print("LL2: ", k.data)
    LL1.tail.next = LL2.head
    return LL1

LL = LinkedList()
for i in range(20):
    LL.prepend(Node(i))

tmp = LL.head
while tmp != None:
    print(tmp.data)
    tmp = tmp.next

Res = Partition(LL,3)
print("----")
for z in Res:
    print(z.data)
print(Res.tail.data)
