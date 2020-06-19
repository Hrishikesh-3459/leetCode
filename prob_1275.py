class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['l' for i in range(3)] for j in range(3)]
        grid[0][2] = 'R'
        grid[1][1] = 'U'
        grid[2][0] = 'M'
        flag = True
        for i in moves:
            if flag == True:
                grid[i[0]][i[1]] = 'A'
                if self.check(grid):
                    return "A"
                flag = False
            elif flag == False:
                grid[i[0]][i[1]] = 'B'
                if self.check(grid):
                    return "B"
                flag = True
        if len(moves) == 9:
            return "Draw"
        return "Pending"
        
    def check(self, grid):
        for i in grid:
            if i[0] == i[1] == i[2]:
                return True
        x = 0
        for j in range(3):
            if grid[x][j] == grid[x + 1][j] == grid[x + 2][j]:
                return True
            elif grid[x][x] == grid[x + 1][x + 1] == grid[x + 2][x + 2]:
                return True
            elif grid[x][x + 2] == grid[x + 1][x + 1] == grid[x + 2][x]:
                return True
            x = 0
        return False
