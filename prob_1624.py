class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == len(set(s)):
            return -1
        ans = 0
        for i, n in enumerate(s):
            stop = s.rindex(n) - 1
            cur = stop - i
            ans = max(ans, cur)
        return ans
