import copy
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # a = list(zip(*A))
        # return a
        ans = []
        counter = [i for i in range(len(A[0]))]
        for i in counter:
            col = []
            for j in A:
                val = j[i]
                col.append(val)
            tmp = copy.copy(col)
            ans.append(tmp)
            col.clear()
        return ans
