def removeDuplicates(nums):
    if(len(nums) == 0):
        return 0
    for i in range(len(nums)-1, 0, -1):
        if (nums[i] == nums[i-1]):
            nums.pop(nums.index(nums[i-1]))

    # print(nums)
    return(len(nums))
        

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))