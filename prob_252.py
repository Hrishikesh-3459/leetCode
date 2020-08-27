class Solution:
    def canAttendMeetings(self, intervals):
        prev = 0
        for i, j in sorted(intervals):
            if i < prev:
                return False
            prev = j
        return True