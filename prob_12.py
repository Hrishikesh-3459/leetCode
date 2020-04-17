def intToRoman(num):
    total = ""
    roman = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000: 'M', 4 : 'IV', 9 : 'IX', 90 : 'XC', 900 : 'CM'}
    if(num in roman):
        return(roman[num])
    
# print(intToRoman(9))
a = 1994
ans = []
for i in range(4):
    temp_num = a%(10**(i+1))
    print("Temp = ", temp_num)
    ans.append(intToRoman(temp_num))
    a = a - temp_num
    # print(a)
out = ""
for i in ans[::-1]:
    out = out + i
print(out)
    

