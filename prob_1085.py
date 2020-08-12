class Solution:
    def sumOfDigits(self, A):
        smol = min(A)
        num = 0
        for i in str(smol):
            num += int(i)
        if num & 1 == 0:
            return 1
        return 0