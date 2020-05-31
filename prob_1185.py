import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        x = calendar.weekday(year, month, day)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[x]
