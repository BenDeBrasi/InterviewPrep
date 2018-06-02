def MyQueue:

    def __init__(self):
        self._s1 = []
        self._s2 = []

    def enqueue(self):
        self._s1.append(data)

    def dequeue(self, data):
        self.transfer()
        return self._s2.pop()

    def peek(self):
        self.transfer()
        return self._s2.pop()

    def transfer(self):
        if self._s2.isEmpty():
            for i in self.s1:
                self._s2.append(i)



