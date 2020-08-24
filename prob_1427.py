class Solution:
    def stringShift(self, s, shift):
        l = len(s)
        for d, amt in shift:
            if d == 0:
                # left
                top = s[:amt]
                rest = s[amt:]
                s = rest + top
            else:
                rem = l - amt
                top = s[:rem]
                rest = s[rem:]
                s = rest + top
        return s