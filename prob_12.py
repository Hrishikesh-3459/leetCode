def intToRoman(num):
    total = ""
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    # print(roman.items())
    if(num in roman):
        return(roman[num])
    # elif()
    
    
# print(intToRoman(9))
ex_num = 1994
len_of_num = len(str(ex_num))
ans = []
for i in range(len_of_num):
    temp_num = ex_num%(10**(i+1))
    print("Temp = ", temp_num)
    ans.append(intToRoman(temp_num))
    ex_num = ex_num - temp_num
    # print(a)


out = ""
for i in ans[::-1]:
    out = out + i
print(out)
    


