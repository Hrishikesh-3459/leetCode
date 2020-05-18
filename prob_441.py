class Solution:
    def arrangeCoins(self, n: int) -> int:
        if (n == 1):
            return 1
        i =  0
        while (n > 0):
            i += 1
            if (n == i):
                return i 
            n -= i

        if (n == i):
            return i
        else:
            return i - 1
