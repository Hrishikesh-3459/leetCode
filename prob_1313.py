class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums), 2):
            val = [nums[i]] * nums[i - 1]
            ans.extend(val)
        return ans
