def longestPalindrome(s):
    x = []
    list_of_palin = []
    for i in s:
        x.append(i)
        if(len(x) > 1):
            if(x == x[::-1]):
                list_of_palin.append(x)
        x = []
    print(list_of_palin)
    return(max(list_of_palin))


print(longestPalindrome("cdxxxxdb"))