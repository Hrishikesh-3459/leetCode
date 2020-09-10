import copy


class Solution:
    def fairCandySwap(self, A, B):
        suma = sum(A)
        sumb = sum(B)
        required_sum = (sumb - suma) // 2
        for i in A:
            if i + required_sum in B:
                return [i, i + required_sum]
