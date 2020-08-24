months = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
class Solution:
    def daysBetweenDates(self, date1, date2):
        x = "1950-01-01"
        dist1 = self.calc_days(x, date1)
        dist2 = self.calc_days(x, date2)
        return abs(dist1 - dist2)
        
        
    def is_leap(self, year):
        year = int(year)
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
        return False
    
    def calc_days(self, x, y):
        x = x.split('-')
        y = y.split('-')
        j = int(y[0])
        i = int(x[0])
        ans = 0
        while i != j:
            if self.is_leap(i):
                ans += 366
            else:
                ans += 365
            i += 1
        k = int(y[1])
        l = int(x[1])
        while k != l:
            if l == 2:
                if self.is_leap(i):
                    ans += 29
                else:
                    ans += 28
            else:
                ans += months[l]
            l += 1
        ans += abs(int(y[2]) - int(x[2]))
        return ans
        