class Solution:
    def freqAlphabets(self, s: str) -> str:
        big = []
        s = list(s)
        while s.count('#'):
            ind = s.index('#')
            vals = int(s[ind - 2] + s[ind - 1])
            big.append(chr(96 + vals))
            s[ind], s[ind - 1], s[ind - 2] = '+', '-', '_'
        ans = ""
        for i in s:
            if i == '_':
                ans += big.pop(0)
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                val = chr(96 + int(i))
                ans += val
        return ans
