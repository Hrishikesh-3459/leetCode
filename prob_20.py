def isValid(s):
    brack = []
    opposite = { ')': '(', '}': '{', ']': '['}  
    ope_n = ['[', '(', '{']
    close = [']', ')', '}']
    if(len(s) == 0):
        return(True)
    # if(s[0] == '}' or s[0] == ')' or s[0] == ']'):
    #     return(False)
    for val in s:
        if((len(brack) == 0) and (val in close)):
            return(False)
        if(val in ope_n):
            brack.append(val)
            print(brack)
        elif(brack[-1] == opposite[val]):
            brack.pop()
            print(brack)
        else:
            return(False)
    if(len(brack) == 0):
        return(True)
    else:
        return(False)
        

print(isValid("[([]])"))

    
