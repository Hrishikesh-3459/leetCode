class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = "{0:b}".format(x)
        b = "{0:b}".format(y)
        width = max(len(a), len(b))
        a = a.zfill(width)
        b = b.zfill(width)
        ans = 0
        for i, j in zip(a, b):
            val = int(i) ^ int(j)
            ans += val
        return ans
