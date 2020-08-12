class Solution:
    def maxNumberOfApples(self, arr):
        big = 5000
        ans = 0
        for i in sorted(arr):
            big -= i
            if big < 0:
                return ans
            ans += 1
        return ans