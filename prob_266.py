class Solution:
    def canPermutePalindrome(self, s):
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        flag = False
        for i in di:
            if di[i] & 1 == 1:
                if flag == True:
                    return False
                flag = True
        return True