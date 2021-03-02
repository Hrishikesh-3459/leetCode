class OrderedStream:

    def __init__(self, n: int):
        self.start = 0
        self.ans = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        pos = idKey - 1
        self.ans[pos] = value
        ret = []
        if self.start == pos:
            i = self.start
            while True:
                ret.append(self.ans[i])
                i += 1
                if i >= len(self.ans):
                    break
                if self.ans[i] == 0:
                    self.start = i
                    break
        return ret
                
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
