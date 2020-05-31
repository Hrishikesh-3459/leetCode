class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        x = S.split('-')
        st = ""
        for i in x:
            st += i
        ans = []
        l = []
        for i in range(len(st) - 1, -1, -1):
            if (len(l) == K):
                y = copy.copy(l)
                ans.extend('-')
                ans.extend(y)
                l.clear()
            
            l.append(st[i])
            
        y = copy.copy(l)
        ans.extend('-')
        ans.extend(y)
        ans_str = ""
        for i in ans[::-1]:
            ans_str += i.upper()
        
        return ans_str.rstrip('-')
        
        
