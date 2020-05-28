class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        ans = []
        for i in range(1, m + 1):
            p.append(i)
        
        for i in range(len(queries)):
            val = queries[i]
            ind = p.index(val)
            ans.append(ind)
            p.remove(val)
            p = [val] + p
            
        return ans
        
