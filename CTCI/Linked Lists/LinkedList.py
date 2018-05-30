class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        if head == None:
            self.size = 0
            self.next = head
        else:
            self.size = 1
            self.next = self.head.next
        if self.head == None:
            self.tail = None
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            self.tail = tmp

    def prepend(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            tmp = self.head
            while tmp != None and tmp.next != None:
                tmp = tmp.next
            tail = tmp

        self.size += 1

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size+=1

    def dele(self):
        
        if self.head == None:
            pass
        else:
            self.head = self.head.next
            size -= 1

    def getSize(self):
        return self.size

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current
            self.current = self.current.next
            return element
