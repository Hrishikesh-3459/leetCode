def intToRoman(num):
    len_of_num = len(str(num))
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    temp_ans = []
    temp_num = []
    for i in range(len_of_num):
        temp_num.append(num%(10**(i+1)))
        num = num - temp_num[i]
    temp_num = temp_num[::-1]
    for j in temp_num:
        if(j in roman):
            temp_ans.append(roman[j])
        else:
            k = j
            while(k != 0):
                if(k >= 1000):
                    k -= 1000
                    temp_ans.append(roman[1000])
                elif(k >= 500 and k < 1000):
                    k -= 500
                    temp_ans.append(roman[500])
                elif(k >= 100 and k < 500):
                    k -= 100
                    temp_ans.append(roman[100])
                elif(k >= 50 and k < 100):
                    k -= 50
                    temp_ans.append(roman[50])
                elif(k >= 10 and k < 50):
                    k -= 10
                    temp_ans.append(roman[10])
                elif(k >= 5 and k < 10):
                    k -= 5
                    temp_ans.append(roman[5])
                else:
                    k -=1
                    temp_ans.append(roman[1])
    out = ''
    for i in temp_ans:
        out = out + i
    return(out)
    


print(intToRoman(1994))