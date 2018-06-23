def ListofDepths(Tree, level):
    if Tree == None:
        return Tree

    qu = queue()
    qu.enqueue(Tree.root)

    while level > 0:
        #Test if leads to going to bottom of tree in single loop if use 'for i in qu'
        for i in range(len(qu)):
            if qu.peek().left != None:
                qu.enqueue(qu.peek().left)
            if qu.peek().right != None:
                qu.enqueue(qu.peek().right)
            qu.dequeue()
        level -=1
        
    listy = LinkedList()
    
    for i in qu:
        qu.dequeue() 
        listy.append(i)

    return listy

