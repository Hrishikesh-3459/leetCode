class Solution:
    def minimumAbsDifference(self, arr):
        di = {}
        arr.sort()
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            val = [arr[i - 1], arr[i]]
            if diff in di:
                di[diff].append(val)
            else:
                di[diff] = list()
                di[diff].append(val)
        smol = min(list(di.keys()))
        return di[smol]