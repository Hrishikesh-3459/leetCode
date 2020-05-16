def getSum(a, b):
    l = []
    if (a < 0 and b < 0):
        for i in range(abs(a)):
            l.append(i)
        for i in range(abs(b)):
            l.append(i)
        return(len(l)*(-1))
    for i in range(max(a,b)):
        l.append(i)
    if (min(a,b) < 0):
        for i in range(abs(min(a,b))):
            l.pop()
    elif (min(a,b) > 0):
        for i in range(min(a,b)):
            l.append(i)
    if (len(l) != 1):    
        return (len(l))
    return 0

print(getSum(-14,16))