class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e_ans = []
        o_ans = []
        for i in A:
            if (i % 2 == 0):
                e_ans.append(i)
            else:
                o_ans.append(i)
        return e_ans + o_ans
        
