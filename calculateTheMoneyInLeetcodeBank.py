class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        lastDay = monday - 1
        ans = 0
        i = 1
        k = 8
        while i <= n:
            if (lastDay + 1) % k == 0:
                k += 1
                monday += 1
                lastDay = monday - 1
            ans += lastDay + 1
            lastDay += 1
            i += 1
        return ans
