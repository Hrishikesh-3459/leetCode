def isValid(s):
    brack = []
    opposite = { ')': '(', '}': '{', ']': '['}  
    ope_n = ['[', '(', '{']
    if(s[0] == '}' or s[0] == ')' or s[0] == ']'):
        return(False)
    for i in range(len(s)):
        if(s[i] in ope_n):
            brack.append(s[i])
        elif(brack[-1] == opposite[s[i]]):
            brack.remove(brack[-1])
        else:
            return(False)
    if(len(brack) == 0):
        return(True)
    else:
        return(False)
        
        

print(isValid("[])"))

    
