class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        y = sorted(list(set(nums)))
        y = y[::-1]
        if (len(y) < 3):
            return max(y)
        else:
            return y[2]
        
