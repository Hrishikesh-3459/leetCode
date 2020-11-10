# Sort Array by Increasing Frequency
class Solution:
    def frequencySort(self, nums):
        x = sorted(nums, key=lambda x: (nums.count(x), -x))
        return x
