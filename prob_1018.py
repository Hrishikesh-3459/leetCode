class Solution:
    def prefixesDivBy5(self, A):
        pref = ""
        ans = []
        while A:
            pref += str(A.pop(0))
            if int(pref, 2) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans