class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        di = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        ans = ""
        for i in num:
            if i not in di:
                return False
            ans += di[i]
        return ans[::-1] == num