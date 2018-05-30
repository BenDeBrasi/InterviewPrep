from LinkedList import *

#Hash table algorithm
def loop_detection(LL):
    items = set([])
    tmp = LL.head
    
    while tmp != None:
        if id(tmp) in items:
            return tmp
        else:
            items.add(id(tmp))
        tmp = tmp.next
    
    return None

#Floyds Cycle Algorithm
def loop_detection1(LL):
    slow = LL.head
    fast = LL.head

    while True:
        slow = slow.next
        if fast == None or fast.next == None:
            return None
        else:
            fast = fast.next.next
        if slow == fast:
            break

    slow = LL.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

LL = LinkedList()
for i in range(20):
    LL.append(Node(i))

LL.tail.next = LL.head.next.next.next
print(loop_detection(LL).data)
