from collections import deque
class FirstUnique:

    def __init__(self, nums):
        self.q = deque(nums)
        self.unq = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self):
        while self.q and not self.unq[self.q[0]]:
            self.q.popleft()
        if self.q:
            return self.q[0]
        return -1

    def add(self, value):
        if value not in self.unq:
            self.q.append(value)
            self.unq[value] = True
        else:
            self.unq[value] = False
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)