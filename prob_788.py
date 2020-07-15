def rotatedDigits(self, N: int) -> int:
    ans = 0
    for i in range(1, N+1):
        x = str(i)
        if '3' in x or '4' in x or '7' in x:
            continue
        p = x
        if '2' in x:
            p = x.replace('2', '5')
        elif '5' in x:
            p = x.replace('5', '2')
        if '6' in x:
            p = x.replace('6', '9')
        elif '9' in x:
            p = x.replace('9', '6')
        if x != p:
            # print(x)
            ans += 1
    return ans