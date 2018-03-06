class Node:
    def __init-__(self):
        

class Queue(list):
    
    def enqueue(self,item):
        return self.append(item)
    
    def dequeue(self):
        if not self:
            return None
        else:
            tmp = self[0]
            self = self[1:]
            return tmp
    
    def isEmpty(self):
        if not self:
            return False
        else:
            return True

def DFS(Node,target):
    
    Q.enqueue(Node)
    
    while Q:
        
        if not Node:
            return False
        elif Node.data == target:
            return True
        
        if Node.state == not_visited:
            Node.state = visited
        else:
            Q.dequeue()
            pass

        Q.dequeue()    
        Q.enqueue(Node.left)
        Q.enqueue(Node.right)

def FindRoute(N1,N2):
    if DFS(N1,N2) or DFS(N2,N1):
        return True
    else:
        return False

print(FindRoute(N1,N2))
