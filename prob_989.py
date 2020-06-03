class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        st = ""
        for i in A:
            st += str(i)
        y = int(st) + K
        ans = []
        for i in str(y):
            ans.append(int(i))
        return ans
        
