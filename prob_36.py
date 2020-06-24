class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            print(i)
        for row in board:
            for elm in row:
                if elm == '.':
                    continue
                x = row.count(elm)
                if x > 1:
                    return False
        cols = list(zip(*board))
        for col in cols:
            for elm in col:
                if elm == '.':
                    continue
                x = col.count(elm)
                if x > 1:
                    return False
        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                l = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in l:
                            return False
                        l.append(board[i][j])
        return True
