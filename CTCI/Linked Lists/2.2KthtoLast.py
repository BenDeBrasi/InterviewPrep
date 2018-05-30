from LinkedList import *

#2 pointers. One set k elements into the LL (later) other at the start(target). Iterate moving each by 1 till later reaches end of LL and return target.
def kth(LL, k):
    
    later = LL.head
    
    for i in range(k):
        later = later.next
    
    target = LL.head
    while later.next != None:
        target = target.next
        later = later.next

    return target


#Recursive solution. Base case is reaching end of list and returning None. Recurse on .next directly after base case check to traverse through whole list. Upon each recursive call resuming remainder of function, increment global variable (count) by 1 and check if k = count. When count = k return that LL.head, otherwise return previous calls return value.

count = 0

#Can change function to use nodes (user has to pass in head of linked list) rather easily and have it be more minorly more efficient since LLs aren't being recreated every call. 
def kthRec(LL,k):
    global count
    if LL.head is None:
        return None

    n = kthRec(LinkedList(LL.head.next),k)
    count += 1 
    if count == k + 1:
        return LL.head
    
    return n

LL= LinkedList()
for i in range(10):
    LL.prepend(Node(i))

for i in LL:
    print(i.data)

print("-----")
print(kthRec(LL,7).data)
