class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        larg = max(nums)
        for i in nums:
            if (i == larg):
                continue
            if (2 * i > larg):
                return -1
        return nums.index(larg)
        
