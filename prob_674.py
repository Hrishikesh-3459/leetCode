class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        stack = [nums[0]]
        le = 0
        for i in nums[1:]:
            if(i > stack[-1]):
                stack.append(i)
            else:
                le = max(le, len(stack))
                stack.clear()
                stack.append(i)
        return max(le, len(stack))
            
