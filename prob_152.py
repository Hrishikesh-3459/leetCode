class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 0
        suffix = 0
        best = float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            best = max(best, prefix, suffix)
        return best
