class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if (k == nums):
            return nums
        di = {}
        for i in nums:
            if (i in di):
                di[i] += 1
            else:
                di[i] = 1
        return heapq.nlargest(k, di.keys(), key = di.get)
