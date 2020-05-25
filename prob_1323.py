class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        str_num = str(num)
        for i in range(len(str_num)):
            if (int(str_num[i]) == 6):
                ans = str_num[:i] + '9' + str_num[i+1:]
                break
        if (len(ans) == 0):
            return num
        return int(ans)
