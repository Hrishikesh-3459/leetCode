from collections import deque
class Solution:
    def maxVowels(self, s, k):
        vowels = ('a', 'e', 'i', 'o', 'u')
        vowels = set(vowels)
        start = 0
        stop = start + k
        arr = list(s)
        q = deque(arr[start : stop])
        ans = 0
        for i in arr[start : stop]:
            if i in vowels:
                ans += 1
        prev = ans
        while stop < len(arr):
            cur = prev
            rem = q.popleft()
            if rem in vowels:
                cur -= 1
            ad = arr[stop]
            if ad in vowels:
                cur += 1
            q.append(ad)
            prev = cur
            ans = max(ans, cur)
            stop += 1
        return ans