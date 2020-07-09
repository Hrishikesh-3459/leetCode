def checkIfCanBreak(s1, s2):
    i = 0
    s1 = sorted(s1)
    s2 = sorted(s2)
    f1 = True
    while i < len(s1):
        if not s1[i] >= s2[i]:
            f1 = False
        i += 1
    i = 0
    f2 = True
    while i < len(s2):
        if not s2[i] >= s1[i]:
            f2 = False
        i += 1
    return f1 or f2