class Solution:
    def anagramMappings(self, A, B):
        di = {}
        for i, j in enumerate(B):
            if j in di:
                di[j].append(i)
            else:
                di[j] = [i]
        ans = []
        for i in A:
            val = di[i].pop()
            ans.append(val)
        return ans