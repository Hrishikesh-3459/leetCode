class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        big = float('-inf')
        ans = ""
        releaseTimes = [0] + releaseTimes
        for n, i in enumerate(keysPressed):
            tmp = releaseTimes[n + 1] - releaseTimes[n]
            if tmp > big:
                big = max(big, tmp)
                ans = i
            elif tmp == big:
                big = max(big, tmp)
                ans = max(ans, i)
        return ans
