def countAndSay(n):
    if(n == 1):
        return("1")
    elif(n == 2):
        return("11")
    else:
        last_res = countAndSay(n - 1)
        i = 0
        ctr = 1
        string = ""
        while(i < len(last_res) - 1):
            if(last_res[i] == last_res[i + 1]):
                ctr += 1
                i += 1
            else:
                string += str(ctr) + last_res[i]
                ctr = 1
                i += 1
        
        return(string)

print(countAndSay(6))
# 12
# 111221