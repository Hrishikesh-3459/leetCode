class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max = maxSize
        

    def push(self, x: int) -> None:
        if (len(self.stack) < self.max):
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        if (k > len(self.stack)):
            self.stack = list(map(lambda x: x + val, self.stack))
        else:
            for i in range(k):
                self.stack[i] += val
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
