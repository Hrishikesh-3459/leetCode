def countSegments(self, s: str) -> int:
    ans = 0
    i = 0
    flag = True
    while i < len(s):
        if not s[i].isspace() and flag == True:
            flag = False
            ans += 1
        elif s[i].isspace() and flag == False:
            flag = True
        i += 1
    return ans