class Solution:
    def gcdOfStrings(self, str1, str2):
        smol = min(len(str1), len(str2))
        ans = 0
        for i in range(1, smol + 1):
            tmp1 = str1[:i]
            tmp2 = str2[:i]
            if tmp1 != tmp2:
                break
            if self.check_concat(str1, str2, i):
                ans = max(ans, i)
        return str1[:ans] if ans > 0 else ""

    def check_concat(self, str1, str2, i):
        tmp1 = str1[:i]
        if tmp1 * (len(str1) // len(tmp1)) != str1:
            return False
        tmp2 = str2[:i]
        if tmp2 * (len(str2) // len(tmp2)) != str2:
            return False
        return True
