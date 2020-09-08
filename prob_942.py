class Solution:
    def diStringMatch(self, S):
        n = len(S)
        x = 0
        ans = []
        for i in S:
            if i == 'I':
                ans.append(x)
                x += 1
            else:
                ans.append(n)
                n -= 1
        for i in range(0, n+1):
            if i not in ans:
                ans.append(i)
        return ans
