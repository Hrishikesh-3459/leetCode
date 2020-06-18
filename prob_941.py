class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        switch = False
        inc = False
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return False
            elif A[i] < A[i-1]  and switch == False:
                switch = True
            elif A[i] > A[i-1] and switch == True:
                return False
            elif A[i] > A[i-1]:
                inc = True
        if switch != True or inc != True:
            return False
        return True
