def singleNumber(nums):
    for i in nums:
        if (nums.count(i) == 1):
            return i


print(singleNumber([4,1,2,1,2]))