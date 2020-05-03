def removeElement(nums, val):
    if(len(nums) == 0):
        return 0
    for i in nums[::-1]:
        if (i == val):
            nums.pop(nums.index(i))
    print(nums)
    return(len(nums))

print(removeElement([0,1,2,2,3,0,4,2], 2))