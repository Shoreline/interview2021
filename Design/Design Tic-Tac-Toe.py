# No need to have a n * n board saved in the class
#   player one +1, player two -1.
#   Just track the sum of each row/column/diag/anti-diag
#   anti-dia: row + col == n - 1
# We don't care about board states. Only need to track all possible winning condidtions
# So, track each row/line/diagonal/anti-diagonal's winning stats
class TicTacToe:

    def __init__(self, n: int):
        self.row, self.col = [0] * n, [0] * n
        self.diag, self.anti_diag, self.n = 0, 0, n

    def move(self, row: int, col: int, player: int) -> int:
        diff = -1 if player == 1 else 1

        # update affected tracks
        self.row[row] += diff
        self.col[col] += diff
        if row == col:  # Move happens on the diagnal line
            self.diag += diff
        if row + col == self.n - 1:  # Move happens on the anti-diagnal line
            self.anti_diag += diff

        # Check if there is a winner
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(
                self.anti_diag) == self.n:
            return player

        return 0

    # Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)