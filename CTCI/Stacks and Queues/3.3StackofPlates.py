def Stack_Of_Plates():
    def __init__(self,limit):
        self._list = []
        self._list.append(stack())
        self._limit = limit
        self._curr_stack = 1

    def push(self,data):
        if self._limit == len(self[len(self)-1]):
            self._curr_stack +=1
            self._list.append(stack())
        self[self._curr_stack].add(data)

    def pop(self):
        if len(self[_curr_stack]) == 0 and len(self._list) > 1:
            self.pop()
            self._curr_stack == 1
        return self[self._curr_stack].pop()

    def popAt(self, index):
        if self._current_stack < index:
            return None
        else:
            return self[index].pop()


