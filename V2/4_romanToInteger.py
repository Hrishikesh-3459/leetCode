class Solution:
    def romanToInt(s):
        di = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
        l = ["I", "X", "C"]
        r = ["V", "L", "D", "X", "C", "M"]
        nor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        le = len(s)
        ans = 0
        i = 0
        while i < le:
            if (s[i] in l) and ((i + 1) < le) and (s[i + 1] in r) and (s[i] + s[i + 1] in di):
                ans += di[s[i] + s[i + 1]]
                i += 1
            else:
                ans += nor[s[i]]
            i += 1
        return ans