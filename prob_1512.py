def numIdenticalPairs(nums):
    ans = 0
    for n,i in enumerate(nums):
        ans += nums[n+1:].count(i)
    return ans