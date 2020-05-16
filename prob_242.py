def isAnagram(s, t):
    if (len(s) != len(t)):
        return False
    x = list(s)
    for i in t:
        if (i not in x):
            return False
        x.pop(x.index(i))
    return True
