def ListofDepths(Tree, level):
    qu = queue()
    qu.enqueue(Tree.root)

    while level > 0:
        for i in range(len(qu)):
            qu.enqueue(qu.peek().left)
            qu.enqueue(qu.peek().right)
            qu.dequeue()
        level -=1
        
    listy = LinkedList()
    
    for i in qu:
        qu.dequeue() 
        listy.append(i)

    return listy

