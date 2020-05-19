class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            centre = (left + right) // 2;
            if (nums[centre] == target):
                return centre
            elif (target > nums[centre]):
                left = centre + 1
            elif (target < nums[centre]):
                right = centre - 1
        return -1
