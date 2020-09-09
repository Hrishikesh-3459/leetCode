class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        i = 0
        count = 0
        while i < len(arr):
            pattern = arr[i: m + i]
            try:
                prev = arr[i - m: i]
            except:
                prev = []
            # print(f"pattern = {pattern}")
            if pattern == prev:
                count += 1
                if count >= k:
                    return True
                i += m
            else:
                count = 1
                i += 1
            # print(f"prev = {prev}")

        return False
