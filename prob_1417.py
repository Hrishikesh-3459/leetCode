class Solution:
    def reformat(self, s: str) -> str:
        if (len(s) == 1):
            return s
        if (s.isalpha()):
            return ""
        if (s.isdigit()):
            return ""
        num = []
        ch = []
        for i in s:
            if (i.isalpha()):
                ch.append(i)
            elif (i.isdigit()):
                num.append(i)


        if (abs(len(num) - len(ch)) > 1):
            return ""

        ans = ""
        if (len(num) == len(ch)):
            for i in range(len(num)):
                ans += num[i] + ch[i]
            return ans

        elif (len(num) > len(ch)):
            for i in range(len(ch)):
                ans += num[i] + ch[i]
            ans += num[-1]
            return(ans)

        else:
            for i in range(len(num)):
                ans += ch[i] + num[i]
            ans += ch[-1]
            return(ans)
       
