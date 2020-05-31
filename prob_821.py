class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ind = []
        for i, ch in enumerate(S):
            if (ch == C):
                ind.append(i)
        ans = []
        for i in range(len(S)):
            tmp = 100000
            for j in ind:
                val = abs(i - j)
                tmp = min(val, tmp)
            ans.append(tmp)
        return ans
