class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if ((len(nums) * len(nums[0])) != (r * c)):
            return nums
        inps = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                inps.append(nums[i][j])
        new = []
        k = 0
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(inps[k])
                k += 1
            new.append(tmp)
        return new
                
