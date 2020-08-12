class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        ans = []
        for i in arr1:
            if i in arr2 and i in arr3:
                ans.append(i)
        return sorted(ans)
            