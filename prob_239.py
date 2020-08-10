from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        start = 0
        stop = start + k
        ans = []
        q = deque(nums[start: stop])
        big = max(q)
        ans.append(big)
        while stop < len(nums):
            rem = q.popleft()
            ad = nums[stop]
            q.append(nums[stop])
            if rem == big:
                big = max(q)
            else:
                big = max(ad, big)
            ans.append(big)
            stop += 1
        return ans