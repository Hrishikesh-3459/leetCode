def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if (nums[i] != val):
            nums[j] = nums[i]
            j += 1
    return j