class Solution:
    def decrypt(self, code, k):
        if k == 0:
            return [0] * len(code)
        if k > 0:
            return self.find_ans(code, k, flag=True)
        return self.find_ans(code, k, flag=False)

    def find_ans(self, code, k, flag):
        if flag == False:
            k *= (-1)
        ans = []
        for n, num in enumerate(code):
            tmp = 0
            for i in range(1, k+1):
                if flag == True:
                    val = (n + i) % len(code)
                else:
                    val = (n - i) % len(code)
                tmp += code[val]
            ans.append(tmp)
        return ans
