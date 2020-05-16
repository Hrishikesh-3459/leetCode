<<<<<<< HEAD
def findcompement(n):
    x = str(bin(n))[2:]
    y = ""
    for i in x :
        if (i == '1'):
            y += '0'
        elif (i == '0'):
            y += '1'
    return(int(y,2))

print(findcompement(1))
=======
class Solution:
    def findComplement(self, num: int) -> int:
        x = str(bin(num))[2:]
        y = ""
        for i in x :
            if (i == '1'):
                y += '0'
            elif (i == '0'):
                y += '1'
        return(int(y,2))
>>>>>>> c342f33c5f94635b5901867b435c2165820ee334
