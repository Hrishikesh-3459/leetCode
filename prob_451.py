class Solution:
    def frequencySort(self, s: str) -> str:
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        val = sorted(di, key = di.get, reverse = True)
        ans = ""
        for i in val:
            ans += i * di[i]
        return ans
        
