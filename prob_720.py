def longestWord(words):
    tmp = sorted(words, key = len)
    ans = []
    while tmp:
        big = tmp.pop()
        i = 0
        flag = True
        while i < len(big):
            if big[ : i + 1] not in words:
                flag = False
                break
            i += 1
        if flag == True:
            ans.append(big)
    ans = sorted(ans, key = len, reverse = True)
    fin = [ans[0]]
    for i in range(1, len(ans)):
        if len(ans[i]) != len(ans[i-1]):
            break
        fin.append(ans[i])
    print(fin)
    return min(fin)