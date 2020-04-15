def isValid(s):
    sq = 0
    curl = 0
    cir = 0
    for i in s:
        if(i == '[' or i == ']'):
            sq += 1
        elif(i == '{' or i == '}'):
            curl += 1
        elif(i == '(' or i == ')'):
            cir += 1
    if((sq%2 == 0) and (curl%2 == 0) and (cir%2 == 0)):
        return(True)
    else:
        return(False)
print(isValid("(]"))

    
