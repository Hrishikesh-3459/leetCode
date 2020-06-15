class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        f = 0
        for i in A:
            if i % 2 == 0:
                f += i
        ans = []
        for val, ind in queries:
            if A[ind] % 2 == 0:
                f -= A[ind]
            A[ind] += val
            if A[ind] % 2 == 0:
                f += A[ind]
            ans.append(f)
        return ans
