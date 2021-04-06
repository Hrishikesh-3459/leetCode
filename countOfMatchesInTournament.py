class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n != 1:
            matches = n // 2
            ans += matches
            n = matches + (n % 2)
        return ans
