def reverseVowels(s):
    vow = []
    x = []
    for i in s:
        if (i in ['a','e','i','o','u']):
            vow.append(i)
    vow.reverse()
    for i in range(len(s)-1,-1,-1):
        if (s[i] in ['a','e','i','o','u']):
            x.append(s.replace(s[i],vow[0],1))
            vow.pop(0)
    print(x)
    return s
    


print(reverseVowels('hello'))