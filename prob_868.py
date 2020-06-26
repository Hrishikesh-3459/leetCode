class Solution:
    def binaryGap(self, N: int) -> int:
        x = bin(N).replace("0b", "")
        print(x)
        if x.count('1') == 0:
            return 0
        ind = []
        for i, n in enumerate(x):
            if n == '1':
                ind.append(i)
        ans = 0
        for i in range(1, len(ind)):
            tmp = ind[i] - ind[i-1]
            ans = max(ans, tmp)
        return ans
