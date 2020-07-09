def camelMatch(queries, pattern):
    ans = []
    for i in queries:
        pat = list(pattern)
        flag = True
        for j in i:
            if not pat and j.isupper():
                ans.append(False)
                flag = False
                break
            try:
                if j.isupper() and pat[0] != j:
                    ans.append(False)
                    flag = False
                    break
                if j == pat[0]:
                    pat.pop(0)
            except IndexError:
                continue
        if pat and flag == True:
            ans.append(False)
            flag = False
        if not pat and flag == True:
            ans.append(True)
    return ans