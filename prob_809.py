class Solution:
    def expressiveWords(self, S, words):
        ans = 0
        count = self.count_freq(S)
        for i in words:
            if set(i) != set(S):
                continue
            tmp = self.count_freq(i)
            flag = False
            if len(tmp) == len(count):
                for l,m in zip(tmp, count):
                    if l > m:
                        flag = True
                        break
                    if l != m and m < 3:
                        flag = True
                        break
                if flag == False:
                    ans += 1
        return ans
            
    def count_freq(self, S):
        count = []
        i = 0
        while i < len(S):
            cur = S[i]
            tmp = 1
            while True:
                if i + 1 < len(S) and cur == S[i+1]:
                    tmp += 1
                    i += 1
                else:
                    count.append(tmp)
                    break
            i += 1
        return count