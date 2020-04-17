def isValid(s):
    x = []
    ope = ['{', '(', '[']
    clos = ['}', ')', ']']
    if(s[-1] in ope):
        return(False)
    if(len(s) == 0):
        return(True)
    for i in s:
        if(i in ope):
            x.append(i)
    # diff = list(set(s)^set(x))
    # print(diff)
    print(x)

isValid("()[]")


