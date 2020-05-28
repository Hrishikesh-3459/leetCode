class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        per = len(arr) * (25 / 100)
        for i in arr:
            if (arr.count(i) > per):
                return i
            
