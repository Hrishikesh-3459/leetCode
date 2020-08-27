class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.big_boy = float('-inf')
        self.smol_boi = float('inf')

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.big_boy = max(self.big_boy, x)
        self.smol_boi = min(self.smol_boi, x)

    def pop(self) -> int:
        x = self.arr.pop()
        try:
            if x == self.smol_boi:
                self.smol_boi = min(self.arr)
            elif x == self.big_boy:
                self.big_boy = max(self.arr)
        except:
            self.big_boy = float('-inf')
            self.smol_boi = float('inf')
        return x
        

    def top(self) -> int:
        return self.arr[-1]

    def peekMax(self) -> int:
        return self.big_boy

    def popMax(self) -> int:
        ind = len(self.arr) - self.arr[::-1].index(self.big_boy) - 1 
        x = self.arr.pop(ind)
        try:
            self.big_boy = max(self.arr)
        except:
            self.big_boy = float('-inf')
        return x
    


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()