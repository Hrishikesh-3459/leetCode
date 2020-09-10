class Solution:
    def validPalindrome(self, s):
        if (s == s[::-1]):
            return True
        start = 0
        stop = len(s) - 1
        while start < stop:
            if s[start] != s[stop]:
                left = s[start:stop]
                right = s[start + 1: stop + 1]
                return left == left[::-1] or right == right[::-1]
            start += 1
            stop -= 1
        return True
