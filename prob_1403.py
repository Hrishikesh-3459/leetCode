class Solution:
    def minSubsequence(self, nums):
        initial_sum = sum(nums)
        sorted_array = sorted(nums)
        ans = []
        ans_sum = 0
        while True:
            element = sorted_array.pop()
            ans.append(element)
            initial_sum -= element
            ans_sum += element
            if ans_sum > initial_sum:
                return ans
