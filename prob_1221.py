class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i = 0
        ans = []
        tmp = ""
        while i < len(s):
            tmp += s[i]
            if tmp.count('L') == tmp.count('R'):
                ans.append(tmp)
                tmp = ""
            i += 1
        print(ans)
        return len(ans)
