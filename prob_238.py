import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        r = [0] * len(nums)
        l[0] = 1
        r[-1] = 1
        ans = [0] * len(nums)
        for i in range(1, len(nums)):
            l[i] = nums[i-1] * l[i-1]
        for i in reversed(range(len(nums) - 1)):
            r[i] = nums[i+1] * r[i+1]
        for i in range(len(nums)):
            ans[i] = l[i] * r[i]
        return ans
