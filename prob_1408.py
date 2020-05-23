class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            count = 1
            for j in words:
                if (i in j):
                    count += 1
                    
            if (count > 2):
                ans.append(i)
                
        return ans
        
