class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.suma = 0
        self.size = size

    def next(self, val):
        self.q.append(val)
        if len(self.q) > self.size:
            self.suma -= self.q.pop(0)
        self.suma += val
        return self.suma / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)