def twoSum(numbers,target):
    out = []
    flag = False
    for num in range(len(numbers)):
        diff = target - numbers[num]
        for j in range(num+1,len(numbers)):
            if (numbers[j] == diff):
                flag = True
                out.append(num + 1)
                out.append(j + 1)
                break
        if (flag == True):
            break
            
    return(out)