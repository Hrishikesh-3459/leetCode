class Solution:
    def numberOfDays(self, Y, M):
        days = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if M in days:
            return days[M]
        if Y % 400 == 0:
            return 29
        if Y % 100 == 0:
            return 28
        if Y % 4 == 0:
            return 29
        return 28