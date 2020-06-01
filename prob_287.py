class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            if (i in di):
                return i
            else:
                di[i] = 1
