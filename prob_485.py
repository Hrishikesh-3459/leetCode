class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if (len(nums) == 1 and nums[0] == 1):
            return 1
        i = 0
        count = 0
        max_count = 0
        while (i < len(nums)):
            if (nums[i] == 1):
                count += 1
            else:
                if (count > max_count):
                    max_count = count
                count = 0
            i += 1
        return max(max_count,count)
