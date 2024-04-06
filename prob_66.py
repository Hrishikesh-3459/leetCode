def plusOne(digits):
    num = ""
    for i in digits:
        num += str(i)
    out = int(num) + 1
    ret = []
    for i in str(out):
        ret.append(i)
    return(ret)
print(plusOne([9]))