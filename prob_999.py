class Solution:
    def numRookCaptures(self, board):
        ans = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    ans += self.check(row, col, board)
        return ans
                    
    def check(self, row, col, board):
        rows = board[row]
        cols = list(zip(*board))[col]
        row_pos = rows.index('R')
        ans = 0
        ans += self.check_pos(row_pos, rows)
        col_pos = cols.index('R')
        ans += self.check_pos(col_pos, cols)
        return ans
        
    def check_pos(self, pos, cord):
        i = 1
        j = -1
        flag1 = True
        flag2 = True
        ans = 0
        while True:
            if flag1 == False and flag2 == False:
                break
            x_pos = (pos + i) if flag1 else False
            x_pos2 = (pos + j) if flag2 else False
            # print(f"for cord = {cord} x_pos = {x_pos}, x_pos2 = {x_pos2}")
            if x_pos:
                if cord[x_pos] == 'p':
                    ans += 1
                    flag1 = False
                if cord[x_pos] == 'B':
                    flag1 = False
            if x_pos2:
                if cord[x_pos2] == 'p':
                    ans += 1
                    flag2 = False
                if cord[x_pos2] == 'B':
                    flag2 = False
            i += 1
            if (pos + i) == len(cord):
                flag1 = False
            j -= 1
            if (pos + j) < 0:
                flag2 = False
        return ans