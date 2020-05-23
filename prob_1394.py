class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = []
        for i in arr:
            if (i == arr.count(i)):
                ans.append(i)
        
        if (len(ans) == 0):
            return -1
        
        return max(ans)
