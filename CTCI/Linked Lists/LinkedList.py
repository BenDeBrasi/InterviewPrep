class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.size = 1
    
    def add(self, node):
        
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
        self.size += 1
    
    def dele(self):
        
        if self.head == None:
            pass
        else:
            self.head = self.head.next
            size -= 1

    def getSize(self):
        return self.size
