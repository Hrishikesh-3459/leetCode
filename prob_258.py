def addDigits(self, num: int) -> int:
        while (len(str(num)) != 1):
            su = 0
            for i in str(num):
                su += int(i)
            num = su
        return (num)
