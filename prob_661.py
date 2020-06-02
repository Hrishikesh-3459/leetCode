import math
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        new_arr = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        for row in range(len(M)):
            for col in range(len(M[0])):
                r = -1
                val = 0
                l = 0
                while (r < 2):
                    c = -1
                    while(c < 2):
                        if (col + c not in range(0, len(M[0])) or row + r not in range(0,                                       len(M))):
                            pass
                        else:
                            val += M[row + r][col + c]
                            l += 1
                        c += 1
                    r += 1
                avg = math.floor(val / l)
                new_arr[row][col] = avg
        return new_arr
                            
