def addBinary(a: str, b: str) -> str:
    int_sum = int(a,2) + int(b,2)
    return(bin(int_sum)[2:])
        