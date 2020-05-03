def searchInsert(nums, target):
    if(len(nums) == 0):
        return 0
    if (target in nums):
        return(nums.index(target))
    for i in nums:
        if (target < i):
            return(nums.index(i))
    return(len(nums))