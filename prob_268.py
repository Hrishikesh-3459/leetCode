def missingNumber(nums):
    for i in range(len(nums)+1):
        if (i not in nums):
            return i
