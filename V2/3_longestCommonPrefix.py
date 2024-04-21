class Solution:
    def longestCommonPrefix(strs):
        ind = 0
        smol_len = 201
        smol_word = ""
        for s in strs:
            if (len(s) < smol_len):
                smol_len = len(s)
                smol_word = s

        while smol_len > 0:
            flag = True
            ans = smol_word[:smol_len]
            for s in strs:
                if s[:smol_len] != ans:
                    flag = False
                    break
            if flag:
                return ans
            smol_len -= 1
        return ""
