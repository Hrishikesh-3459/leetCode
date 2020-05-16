def findcompement(n):
    x = str(bin(n))[2:]
    y = ""
    for i in x :
        if (i == '1'):
            y += '0'
        elif (i == '0'):
            y += '1'
    return(int(y,2))

print(findcompement(1))