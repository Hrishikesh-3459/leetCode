class Solution:
    def isArmstrong(self, N: int):
        val = 0
        k = len(str(N))
        for i in str(N):
            val += int(i) ** k
        return val == N