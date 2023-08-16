# No need to have a n * n board saved in the class
#   player one +1, player two -1.
#   Just track the sum of each row/column/diagonal/anti-diagonal
#   anti-dia: row + col == n - 1
# We don't care about board states. Only need to track all possible winning conditions
# So, track each row/line/diagonal/anti-diagonal's winning stats
class TicTacToe:

    def __init__(self, n: int):
        self.rows, self.cols = [0] * n, [0] * n
        self.diag, self.anti_diag, self.n = 0, 0, n

    def move(self, row: int, col: int, player: int) -> int:
        diff = -1 if player == 1 else 1

        # update affected tracks
        self.rows[row] += diff
        self.cols[col] += diff
        if row == col:  # Move happens on the diagonal line
            self.diag += diff
        if row + col == self.n - 1:  # Move happens on the anti-diagonal line
            self.anti_diag += diff

        # Check if there is a winner
        if self.n in (abs(self.rows[row]), abs(self.cols[col]), abs(self.diag), abs(self.anti_diag)):
            return player

        return 0

    # Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

#dydx interview
"""
Tic tac toe
simulateGame(n: int)
n x n board
2 AI players - play randomly


3 ways to win:
- n in a row
- n in a column
- n in a diagonal

"""

# import random
#
#
# def simulateGame(n):
#     print("start")
#
#     stats = [[0] * n for _ in range(n)]
#
#     # the sum of values in each line
#     # in total 2n + 2 lines
#     rows = [0] * n
#     cols = [0] * n
#     diag, adiag = 0, 0
#
#     def print_stats():
#         print("------------------")
#         for i in range(len(stats)):
#             print(stats[i])
#
#     def move(i, j, player):
#         nonlocal diag
#         nonlocal adiag
#         if 0 <= i <= n and 0 <= j <= n:
#             stats[i][j] = player
#
#             rows[i] += player
#             cols[j] += player
#
#             if i == j:
#                 diag += player
#             if i + j == n - 1:
#                 adiag += player
#
#     def win(i, j):
#         if abs(rows[i]) == n or abs(cols[j]) == n or abs(diag) == n or abs(adiag) == n:
#             return True
#         return False
#
#     def moves():
#         res = []
#         for i in range(n):
#             for j in range(n):
#                 res.append((i, j))
#         random.shuffle(res)
#         return res
#
#     moves = moves();
#     player = 1  # two players are 1 and -1
#     for i, j in moves:
#         move(i, j, player)
#         print_stats()
#
#         if (win(i, j)):
#             return player
#
#         player = -player
#
#     return 0  # tie
#
#
# print(simulateGame(3))