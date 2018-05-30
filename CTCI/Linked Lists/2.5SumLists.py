from LinkedList import *
#Numbers going backwards
def reverse_order(LL1,LL2):
    if LL1 == None:
        return LL2
    elif LL2 == None:
        return LL1
    else:
        return rev_order_rec(LL1,LL2,0)

def rev_order_rec(LL1,LL2,carry):
    if (LL1 == None or LL1.head == None) and (LL2 == None or LL2.head == None):
        return LinkedList()    
    value = 0
    if LL1 == None or LL1.head == None:
        value = LL2.head.data
    elif LL2 == None or LL2.head == None:
        value = LL1.head.data
    else:
        value = LL1.head.data + LL2.head.data
    value += carry
    tmp = value
    
    if value >= 10:
        carry = 1
        value = value % 10
    else:
        carry = 0

    if LL1 == None or LL1.head == None:
        res = rev_order_rec(None,LinkedList(LL2.head.next),carry)
    elif LL2 == None or LL2.head == None:
        res = rev_order_rec(LinkedList(LL1.head.next),None,carry)
    else:
        res = rev_order_rec(LinkedList(LL1.head.next), LinkedList(LL2.head.next), carry)

    n = Node(value)
    print("curr value:" , n.data)
    if res.head == None and tmp >= 10:
        m = Node(1)
        res.append(m)
    res.append(n)
    return res

carry = 0
#Numbers going forward
def forward_order(LL1,LL2):
    if LL1.size < LL2.size:
        pad(LL1,LL2)
    elif LL1.size > LL2.size:
        pad(LL2,LL1)
    
    res = add(LL1, LL2)
    if has_carry(LL1,LL2) or carry:
        res.prepend(Node(1))
    return res

def add(LL1,LL2):
    
    global carry
    print("carry: ",carry)
    if LL1.head == None and LL2.head == None:
        return LinkedList()

    res = add(LinkedList(LL1.head.next), LinkedList(LL2.head.next))
    value = LL1.head.data + LL2.head.data
    
    if carry == 0:
        print(LL1.head.data,LL2.head.data)
        value += has_carry(LL1,LL2)
    else:
        value += carry

    if value >= 10:
        value = value % 10
        carry = 1
    else:
        carry = 0

    n = Node(value)
    res.prepend(n)
    return res

def pad(smaller, larger):

    for i in range(larger.size -smaller.size):
        smaller.prepend(Node(0))
    return 

def has_carry(LL1,LL2):
    if LL1.head == None or LL2.head == None:
        pass
    elif LL1.head.next == None or LL2.head.next == None:
        pass
    else:
        if LL1.head.next.data + LL2.head.next.data >= 10:
            return 1
    return 0

LL1 = LinkedList()
LL2 = LinkedList()
LL1.prepend(Node(6))
LL1.prepend(Node(7))
LL1.prepend(Node(9))
LL2.prepend(Node(9))
LL2.prepend(Node(9))
ans = reverse_order(LL1,LL2)

for i in LL1:
    print(i.data)

print("----")
for j in LL2:
    print(j.data)
print("----")
for k in ans:
    print(k.data)
