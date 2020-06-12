class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        big_boi = max(nums)        
        size = len(nums)
        count = [0] * (big_boi + 1)
        out = [0] * size
        for i in nums:
            count[i] += 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        i = size - 1
        while i >= 0:
            out[count[nums[i]] - 1] = nums[i]
            count[nums[i]] -= 1
            i -= 1
            
        for i in range(size):
            nums[i] = out[i]
