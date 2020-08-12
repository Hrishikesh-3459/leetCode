class Solution:
    def isMajorityElement(self, nums, target):
        return nums.count(target) > len(nums) / 2