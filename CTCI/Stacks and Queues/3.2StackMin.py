class stack_min:
    num_of_stacks = 0    
    def __init__(self):
        self.top = None       
        self.min_stack = []
        stack_min.num_of_stacks+=1
    
    class stack_node:
        def __init__(self,data= None):
            self.data = data
            self.next = None
    

    def push(self,data):
        if self == None:
            return None
        if self.top == None:
            self.min_stack.append(data)
        n = stack_min.stack_node(data)
        n.next = self.top
        self.top = n
        if n.data < self.min_stack[len(self.min_stack) -1]:
            self.min_stack.append(self.top.data)

    def pop(self):
        if self.isEmpty:
            return None
    
        tmp = self.top
        if tmp.data == self.min_stack[len(self.min_stack)-1]:
            self.min_stack.pop()
        self.top = self.tmp.next
        return tmp

    def minn(self):
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack[len(self.min_stack)-1]

    def peek(self):
        return self.top.data

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

stack = stack_min()
for i in range(1,20):
    stack.push(i)
stack.push(-1)
print(stack.minn())
