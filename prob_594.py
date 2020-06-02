class Solution:
    def findLHS(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            if (i in di):
                di[i] += 1
            else:
                di[i] = 1
        mx = 0 
        for key in sorted(di):
            if ((key + 1) in di):
                tmp = di[key] + di[key+1]
                mx = max(mx, tmp)
        return mx
