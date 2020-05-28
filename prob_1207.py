class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        di = {}
        for i in arr:
            if (i in di):
                di[i] += 1
            else:
                di[i] = 1
        x = di.values()
        if (len(set(x)) == len(x)):
            return True
        return False
