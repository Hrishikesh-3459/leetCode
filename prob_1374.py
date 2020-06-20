class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n
        st = 'a' * (n-1)
        return st +'b'
