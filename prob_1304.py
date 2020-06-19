class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        if n % 2 == 1:
            ans = [0]
        else:
            ans = []
        k = 1
        while len(ans) != n:
            val = k * (-1)
            ans.append(val)
            ans.append(k)
            k += 1
        return ans
