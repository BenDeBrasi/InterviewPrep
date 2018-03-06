class Stack(list):
    
    def isEmpty(self):
        return not self
    
    def push(self,item):
        return self.append(item)
    
    def peek(self):
        if not self:
            return None
        else:
            return self[:len(self)-1]

def sortStack(stack):
    tmp = Stack([])
    while stack:
        curr = stack.pop()
        if not tmp or curr <= tmp[len(tmp)-1]:
            tmp.append(curr)
        else:
            while tmp and tmp[len(tmp)-1] < curr:
                stack.push(tmp.pop())
            tmp.push(curr)

    for ele in tmp:
        stack.push(ele)

    return stack
HI = Stack([9,3,1,2,5,6,3,3])
print(sortStack(HI))
print(sortStack(HI).pop())

