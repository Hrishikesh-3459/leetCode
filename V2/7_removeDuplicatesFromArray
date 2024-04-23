def removeDuplicates(nums):
        le = len(nums)
        if le == 1:
            return 1
        i = 1
        while i < le:
            if (nums[i] == nums[i - 1]):
                x = nums.pop(i)
                le -= 1
            else:
                i += 1
        return len(nums)