class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.mat = [[0 for i in range(n)]for j in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.mat[row][col] = player
        # print(self.mat)
        for row in self.mat:
            if all(map(lambda j: j == 1, row)):
                return 1
            if all(map(lambda j: j == 2, row)):
                return 2
        for col in zip(*self.mat):
            if all(map(lambda j: j == 1, col)):
                return 1
            if all(map(lambda j: j == 2, col)):
                return 2
        flag1 = [True, True]
        flag2 = [True, True]
        n = len(self.mat)
        for i in range(n):
            if self.mat[i][i] != 1:
                flag1[0] = False
            if self.mat[i][n - i - 1] != 1:
                flag1[1] = False
            if self.mat[i][i] != 2:
                flag2[0] = False
            if self.mat[i][n - i - 1] != 2:
                flag2[1] = False
        if flag1[0] or flag1[1]:
            return 1
        if flag2[0] or flag2[1]:
            return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
