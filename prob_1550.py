class Solution:
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        start = 0
        stop = start + 3
        q = arr[start : stop]
        if self.count_odd(q):
                return True
        while stop < len(arr):
            q.pop(0)
            q.append(arr[stop])
            stop += 1
            if self.count_odd(q):
                return True
        return False
        
    def count_odd(self, arr):
        if arr[0] & 1 == 1 and arr[1] & 1 == 1 and arr[2] & 1 == 1:
            return True
        return False