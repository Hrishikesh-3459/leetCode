class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if (nums[j] < nums[i] and nums[j] != nums[i]):
                    temp += 1
            ans.append(temp)
        
        return ans
