class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if sorted(s) == sorted(t):
            return 0
        s_di = {}
        for i in s:
            if i in s_di:
                s_di[i] += 1
            else:
                s_di[i] = 1
        ans = 0
        for i in s_di:
            if i in t:
                x = t.count(i)
                val = s_di[i] - x
                if val > 0:
                    ans += val
            else:
                ans += s_di[i]
        return ans
