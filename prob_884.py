class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = A.split()
        b = B.split()
        tot = a + b
        di = {}
        bi = {}
        for i in a:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
                bi[i] = 0
        for i in b:
            if i in bi:
                bi[i] += 1
            else:
                bi[i] = 1
                di[i] = 0
        ans = []
        for i in tot:
            if (di[i] == 1 and bi[i] == 0) or (bi[i] == 1 and di[i] == 0):
                ans.append(i)
        return ans
