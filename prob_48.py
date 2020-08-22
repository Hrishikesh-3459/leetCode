class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*matrix))
        for i, n in enumerate(matrix):
            x = list(n)
            matrix.pop(i)
            x.reverse()
            matrix.insert(i, x)