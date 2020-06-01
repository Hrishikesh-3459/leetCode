class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = 0
        for i in range(1, len(A)):
            if (A[i] > A[i - 1]):
                flag += 1
                break
        for j in range(1, len(A)):
            if (A[j] < A[j - 1]):
                flag += 1
                break
        if (flag == 2):
            return False
        return True
        
