class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if (n == 0):
            return True
        i = 0
        while i < len(f):
            if (f[i] == 0 and (i == 0 or f[i - 1] == 0) and (i == len(f) - 1 or f[i + 1] == 0)):
                n -= 1
                f[i] = 1
            if (n == 0):
                return True
            i += 1
        return False
