import math
class Solution:
    def isUgly(self, num: int) -> bool:
        if (num <= 0):
            return False
        ugly = [2, 3, 5]
        ans = []
        while num % 2 == 0:
            ans.append(2)
            num = num / 2
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                ans.append(i)
                num = num / i
        if (num > 2):
            ans.append(num)
        # print(ans)
        for i in ans:
            if (int(i) not in ugly):
                return False
        return True
