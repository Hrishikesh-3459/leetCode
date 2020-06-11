class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = {}
        for i in range(lo, hi+1):
            val = self.getpower(i)
            if val in ans:
                ans[val].append(i)
            else:
                ans[val] = [i]
        a = []
        for i in sorted(ans):
            a.extend(ans[i])
        return a[k-1]
        
    def getpower(self, x):
        ans = 0
        while x != 1:
            if x % 2 == 0:
                x /= 2
                ans += 1
            else:
                x = 3 * x + 1
                ans += 1
        return ans
