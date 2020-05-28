class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = {}
        for i in sorted(arr):
            if (i not in ans):
                ans[i] = len(ans) + 1
        return map(ans.get, arr)
            
