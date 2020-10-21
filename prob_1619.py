class Solution:
    def trimMean(self, arr) -> float:
        n = len(arr)
        five_percent = int(n * (5 / 100))
        n -= (2 * five_percent)
        arr.sort()
        for i in range(five_percent):
            arr.pop()
            arr.pop(0)
        return sum(arr) / n
