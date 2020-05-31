flag = True
        for i in nums:
            if (i > 0):
                flag = False
                break
        if (flag == True):
            return max(nums)
        ans = []
        tmp_arr = []
        for i in nums:
            if (i < 0):
                x = copy.copy(tmp_arr)
                ans.append(x)
                if ((sum(tmp_arr) + i) >= 1):
                    tmp_arr.append(i)
                else:
                    tmp_arr.clear()
            else:
                tmp_arr.append(i)

        x = 0
        if (ans):
            x = max(list(map(sum, ans)))
        return max(x, sum(tmp_arr))
