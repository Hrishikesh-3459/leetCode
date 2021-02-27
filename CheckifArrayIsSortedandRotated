class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] < 0:
                # print(nums[i + 1])
                flag += 1
                if flag == 2:
                    return False
        if nums[0] - nums[-1] < 0:
            flag += 1
            if flag == 2:
                return False
        return True
