class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        str_num = []
        ans = []
        for i in range(left, right+1):
            str_num.append(str(i))
        for i in str_num:
            flag = True
            if ('0' in i):
                continue
            for j in i:
                if (int(i) % int(j) != 0):
                    flag = False
            if (flag == True):
                ans.append(i)

        return(ans)
