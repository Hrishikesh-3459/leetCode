def containsDuplicate(nums):
    x = set (nums)
    if (len(nums) == len(x)):
        return False
    else:
        return True