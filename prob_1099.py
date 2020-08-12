class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()
        for i in range(K-1, 0, -1):
            if self.check_sum(A, i):
                return i
        return -1
    
    def check_sum(self, arr, k):
        low = 0
        high = len(arr) - 1
        while low < high:
            suma = arr[low] + arr[high]
            if suma == k:
                return True
            elif suma > k:
                high -= 1
            else:
                low += 1
        return False