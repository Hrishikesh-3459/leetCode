def romanToInt(s):
    total = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    if(len(s) == 1):
        total += roman[s[i]]
    while(i < len(s) - 1):
        if(s[i] == 'I' and (s[i + 1] == 'X' or s[i + 1] == 'V')):
                total = total + (roman[s[i + 1]] - roman[s[i]])
                i += 1
        elif(s[i] == 'X' and (s[i + 1] == 'C' or s[i + 1] == 'L')):
                total = total + (roman[s[i + 1]] - roman[s[i]])
                i += 1
        elif(s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                total = total + (roman[s[i + 1]] - roman[s[i]])
                i += 1
        else:
            total += roman[s[i]]
        i += 1
        if(i == len(s) - 1):
            total += roman[s[i]]
    return(total)
print(romanToInt("D"))





