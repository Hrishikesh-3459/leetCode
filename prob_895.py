class FreqStack:

    def __init__(self):
        self.stack = []
        self.di = {}

    def push(self, x: int) -> None:
        self.stack.append(x)
        if (x in self.di):
            self.di[x] += 1
        else:
            self.di[x] = 1
        

    def pop(self) -> int:
        big = max(self.di.values())
        for i in self.stack[::-1]:
            if (self.di[i] == big):
                ind = len(self.stack) - self.stack[::-1].index(i) - 1 
                self.stack.pop(ind)
                self.di[i] -= 1
                return i
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
