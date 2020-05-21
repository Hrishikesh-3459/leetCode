class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        x = sorted(nums)
        return max((x[0] * x[1] * x[-1]), (x[-1] * x[-2] * x[-3]))
