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
