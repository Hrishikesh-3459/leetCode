class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in A:
            x = i[::-1]
            for n, i in enumerate(x):
                if i == 1:
                    x[n] = 0
                elif i == 0:
                    x[n] = 1
            ans.append(x)
        return ans
                
