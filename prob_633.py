import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if (c == 1 or c == 0):
            return True
        a = 0
        while a ** 2 <= c:
            b = math.sqrt(c - (a ** 2))
            if b == int(b):
                return True
            a += 1
        return False
