class Solution:
    def diagonalSort(self, mat):
        m = len(mat)
        n = len(mat[0])
        check = [[False for i in range(n)]for j in range(m)]
        i = 0
        j = 0
        while self.check_if_over(check) == False and i < m and j < n:
            row = i
            col = j
            cur = [mat[row][col]]
            if check[row][col] == True:
                j += 1
                if j == n:
                    j = 0
                    i += 1
                    if i == m:
                        break
                continue
            check[row][col] = True
            flag = True
            while True:
                row += 1
                col += 1
                if row < m and col < n:
                    cur.append(mat[row][col])
                    check[row][col] = True
                else:
                    break
            cur.sort()
            row -= 1
            col -= 1
            while row >= i and col >= j and cur:
                mat[row][col] = cur.pop()
                row -= 1
                col -= 1
            j += 1
            if j == n:
                j = 0
                i += 1
                if i == m:
                    break
        return mat

    def check_if_over(self, check):
        for i in check:
            if False in i:
                return False
        return True
