import copy 

def removeElement(nums, val):
    if(len(nums) == 0):
        return 0
    inputs = copy.copy(nums)
    for i in inputs:
        if (i == val):            
            nums.pop(nums.index(i))
    print(nums)
    return(len(nums))

print(removeElement([0,1,2,2,3,2,4,2,2], 2))