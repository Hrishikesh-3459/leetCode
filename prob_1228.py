class Solution:
    def missingNumber(self, arr):
        if arr[1] < arr[0]:
            arr = arr[::-1]
        di = {}
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            di[d] = [arr[i], arr[i-1]]
        big = max(di.keys())
        return min(di[big]) + (big // 2)