from collections import deque
import copy
class Solution:
    def medianSlidingWindow(self, nums, k):
        start = 0
        stop = start + k
        l = nums[start : stop]
        q = deque(l)
        ans = []
        k = copy.copy(list(q))
        ans.append(self.findMedian(k))
        while stop < len(nums):
            q.popleft()
            q.append(nums[stop])
            stop += 1
            k = copy.copy(q)
            ans.append(self.findMedian(list(k)))
        return ans
            

        
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        middle = n // 2
        if n & 1 == 0:
            median = (arr[middle - 1] + arr[middle]) / 2
        else:
            median = arr[middle]
        return median
    