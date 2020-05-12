def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
        if (i == 0):
            nums.pop(nums.index(i))
            nums.append(i)
