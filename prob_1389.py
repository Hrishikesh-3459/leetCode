class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        i = 0
        while (i< len(nums)):
            target.insert(index[i], nums[i])
            i += 1
            
        return target
