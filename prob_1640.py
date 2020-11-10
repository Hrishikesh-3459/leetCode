# Check Array Formation Through Concatenation
class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        all_pieces = set()
        for p in pieces:
            all_pieces.update(set(p))
        for i in arr:
            if i not in all_pieces:
                return False

        for p in pieces:
            prev = float('-inf')
            for i in p:
                cur = arr.index(i)
                if cur < prev:
                    return False
                if prev > -1:
                    if abs(cur - prev) != 1:
                        return False
                prev = cur
        return True
