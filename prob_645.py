class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        big = len(nums)
        for i in nums:
            if nums.count(i) == 2:
                ans.append(i)
                break
        nums.remove(ans[0])        
        cur_sum = sum(nums)
        act_sum = (big * (big + 1)) // 2
        sec = abs(cur_sum - act_sum)
        ans.append(sec)
        return ans
