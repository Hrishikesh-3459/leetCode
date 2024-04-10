def twoSum(self, nums, target):
        diffs = {}
        for i,n in enumerate(nums):
            diff = target - n
            if (diff in diffs):
                return [i, diffs[diff]]
            else:
                diffs[n] = i