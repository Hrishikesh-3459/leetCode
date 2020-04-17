def romanToInt(s):
    total = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    skip_loop = False
    for i in range((len(s)-1), -1, -1):
        if(skip_loop == True):
            skip_loop = False
            continue
        if(s[i] == 'X' or s[i] == 'V'):
            if(s[i-1] == 'I'):
                total = total + (roman[s[i]] - roman[s[i-1]])
                skip_loop = True
        elif(s[i] == 'C' or s[i] == 'L'):
            if(s[i-1] == 'X'):
                total = total + (roman[s[i]] - roman[s[i-1]])
                skip_loop = True
        elif(s[i] == 'D' or s[i] == 'M'):
            if(s[i-1] == 'C'):
                total = total + (roman[s[i]] - roman[s[i-1]])
                skip_loop = True
        if(skip_loop == False):
            total = total + roman[s[i]]
        if(i == 1 and skip_loop == False):
            total = total + roman[s[0]]
            skip_loop = True
    return(total)
print(romanToInt("MCMXCIV"))




