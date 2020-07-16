def convertToBase7(num):
    if num == 0:
        return "0"
    ans = ""
    flag = False
    if num < 0:
        flag = True
        num *= (-1)
    while num > 0:
        ans += str(num % 7)
        num //= 7
    if flag == True:
        return ('-' + ans[::-1])
    else:
        return ans[::-1]