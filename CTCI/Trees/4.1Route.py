def Route(NodeA, NodeB):
    
    QA = queue()
    QB = queue()

    QA.append(NodeA)
    QB.append(NodeB)

    while QA.peek() != None and QB.peek() != None:
        
        
        if QA.peek() == QB.peek() or QA.peek().state == True or QB.peek().state == True:
            return True
        else:
            QA.peek().state = True
            QB.peek().state = True

            for i in QA.peek().adj:
                QA.enqueue(i)
            QA.dequeue()

            for i in QB.peek().adj:
                QB.enqueue(i)
            QB.dequeue()

    return False

def RouteHash(NodeA, NodeB):
    QA = queue()
    QB = queue()

    QA.append(NodeA)
    QB.append(NodeB)
    
    refs = set([])

    while QA.peek() != None and QB.peek() != None:

        if QA.peek() == QB.peek() or id(QA.peek()) in refs or id(QB.peek()) in refs:
            return True
        else:
            dic.add(id(QA.peek()))
            dic.add(id(QB.peek()))
            
            for i in QA.peek().adj:
                QA.enqueue(i)
            QA.dequeue()
            
            for i in QB.peek().adj:
                QB.enqueue(i)
            QB.dequeue()

    return False





