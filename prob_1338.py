class Solution:
    def minSetSize(self, arr) -> int:
        di = {}
        for i in arr:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        values = sorted(list(di.values()))[::-1]
        n = len(arr)
        suma = 0
        for i in range(len(values)):
            suma += values[i]
            if suma >= (n // 2):
                return (i+1)
