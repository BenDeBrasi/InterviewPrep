def DelMidNode(n):
    n.data = n.next.data
    n.next = n.next.next
