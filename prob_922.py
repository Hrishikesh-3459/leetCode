class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        e = []
        o = []
        ans = []
        for i in A:
            if (i % 2 == 0):
                e.append(i)
            else:
                o.append(i)
        for j in range(len(A)):
            if (j % 2 == 0):
                ans.append(e.pop())
            else:
                ans.append(o.pop())
        return ans
            
