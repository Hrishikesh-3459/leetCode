class Solution:
    def generatePossibleNextMoves(self, s):
        q = list(s[0:2])
        ans = []
        i = 2
        while i <= len(s):
            if self.check(q):
                start = i - 2
                val = s[:start] + '--' + s[i:]
                ans.append(val)
            q.pop(0)
            try:
                q.append(s[i])
            except IndexError:
                break
            i += 1
        return ans
            
        
        
    def check(self, q):
        return q[0] == q[1] == '+'