def convertToTitle(n):
    print(chr(int(64 + n)))
    

num = 28
for i in range(3):
    convertToTitle(num % 26)
    num -= num - (num % 26)
    
# checking