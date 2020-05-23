class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        di = {}
        n = 0
        for i in mat:
            di[n] = i.count(1)
            n += 1
        ans = []
        x = 0
        while (len(ans) != k):
            for i in di:
                if (di[i] == x):
                    if (len(ans) == k):
                        break
                    ans.append(i)
            x += 1
        return ans
            
