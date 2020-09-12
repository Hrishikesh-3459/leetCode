class Solution:
    def findRelativeRanks(self, nums):
        x = sorted(nums, reverse=True)
        ans = []
        for i in nums:
            j = x.index(i)
            if j == 0:
                ans.append("Gold Medal")
            elif j == 1:
                ans.append("Silver Medal")
            elif j == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(j+1))
        return ans
