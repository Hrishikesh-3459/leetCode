def isValid(S):
    i = 0
    while True:
        S = S.replace("abc", "")
        if not S:
            return True
        i += 1
        if i > 20000:
            return False