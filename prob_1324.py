class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        x = s.split()
        longest = len(max(x, key = len))
        k = 0
        while k < longest:
            tmp = ""
            for i in x:
                if len(i) <= k:
                    tmp += " "
                else:
                    tmp += i[k]
            ans.append(tmp.rstrip())
            k += 1
        return ans
