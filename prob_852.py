class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        big = max(A)
        return A.index(big)
        
