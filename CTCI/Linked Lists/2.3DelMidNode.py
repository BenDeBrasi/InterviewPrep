#Pass in node to be erased. Set its data to the next nodes data and then set its .next to next nodes .next.

def DelMidNode(n):
    n.data = n.next.data
    n.next = n.next.next
