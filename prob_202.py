def isHappy(n):
    q = 0
    while (q < 50):
        s = 0
        for i in str(n):
            s += int(i) ** 2
        n = s
        if (n == 1):
            return True
        q += 1
    return False
