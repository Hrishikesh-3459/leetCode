def majorityElement(nums):
  nums.sort()
  return nums[len(nums)//2]
    #for i in nums:
        #if (nums.count(i) > len(nums)/2):
            #return i
