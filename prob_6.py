def convert(s, numRows):
    # nums = []
    out = ""
    for i in range(0, len(s), 4):
        out = out + s[i]
    for i in range(1, len(s), 2):
        out = out + s[i]
    for i in range(2, len(s), 4):
        out = out + s[i]
    print(out)
    # The output letters have a pattern like 5,3,1
    # The above code will work when the inpRows is an odd number
    
convert("PAYPALISHIRING", 4)