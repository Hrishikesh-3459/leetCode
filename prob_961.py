class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A) // 2
        for i in A:
            if (A.count(i) == n):
                return i
