class Solution:
    def toHexspeak(self, num):
        x = (hex(int(num)))
        check = {"A", "B", "C", "D", "E", "F", "I", "O"}
        x = x.replace('0', 'O')
        x = x.replace('1', 'I')
        x = x.upper()
        for i in x[2:]:
            if i not in check:
                return "ERROR"
        return x[2:]