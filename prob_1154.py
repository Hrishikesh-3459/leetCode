class Solution:
    def dayOfYear(self, date: str) -> int:
        di = {1: 31, 2: [28, 29], 3: 31, 4:30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        x = date.split('-')
        year = int(x[0])
        month = int(x[1])
        day = int(x[2])
        if (year % 400 == 0):
            leap = True
        elif (year % 100 == 0):
            leap = False
        elif (year % 4 == 0):
            leap = True
        else :
            leap = False
        if (month == 1):
            return day
        else:
            ans = day
            for i in range(month-1, 0, -1):
                if (i == 2):
                    if (leap == True):
                        ans += di[i][1]
                    else:
                        ans += di[i][0]
                else:
                    ans += di[i]
        return ans
        
