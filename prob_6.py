from itertools import cycle
def convert(s,numRows):
    out = ""
    row_nums = list(range(0, numRows))
    row_rev = list(range(numRows-2,0,-1))
    row_nums.extend(row_rev)
    pool = cycle(row_nums)
    rows = [[0 for i in range(0)] for j in range(numRows)] 
    for i in range(0, len(s)):
        rows[next(pool)].append(s[i])
    
    for i in range(numRows):
        for j in range(len(rows[i])):
            out += str(rows[i][j])
    return(out)


print(convert("PAYPALISHIRING", 1))
