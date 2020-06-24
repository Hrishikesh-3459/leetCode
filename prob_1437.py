class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        di = []
        for n, i in enumerate(nums):
            if i == 1:
                di.append(n)
        print(di)
        for i in range(1, len(di)):
            x = abs(di[i] - di[i-1]) - 1
            if x < k:
                return False
        return True
            
