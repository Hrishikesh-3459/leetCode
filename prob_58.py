def lengthOfLastWord(s):
    count = 0
    if(len(s) == 0):
        return(0)
    try:
        while(s[-1] == ' '):
            s = s[:-1]
    except IndexError:
        return(0)
    print(s)
    for i in range((len(s)-1), -1, -1):
        print(s[i])
        if(s[i] == ' '):
            break
        else:
            count += 1
    return(count)
print(lengthOfLastWord("    "))

# stre = "ramu ki jai"
# st = stre[-1]
# print(st)