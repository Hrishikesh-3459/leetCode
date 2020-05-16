def firstUniqChar(s):
    new = []
    for i in s:
        if (i not in s[s.index(i)+1:len(s)]):
            new.append(i)
    if (new[0] in s):
        return(s.index(new[0]))
    else :
        return -1

print(firstUniqChar("leetcode"))