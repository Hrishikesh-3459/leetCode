class Solution:
    def longestPalindrome(self, s: str) -> int:
        if(s == s[::-1]):
            return len(s)
        di = {}
        for i in s:
            if (i in di):
                di[i] += 1
            else:
                di[i] = 1
        odd_count = -1
        for i in di:
            if (di[i] % 2 == 1):
                odd_count += 1
        if (odd_count > 0):
            return len(s) - odd_count
        return len(s)
        
