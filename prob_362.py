class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.arr.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start = timestamp - 300
        ans = 0
        for i in self.arr:
            if i <= start:
                ans += 1
        return len(self.arr) - ans


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)