class Solution:
    def findKthPositive(self, arr, k):
        missing = []
        i = 1
        while True:
            if i in arr:
                i += 1
                continue
            else:
                missing.append(i)
                if len(missing) == k:
                    return missing[k-1]
                i += 1
        