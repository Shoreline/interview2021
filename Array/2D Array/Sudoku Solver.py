# Different from normal backtracking, the pre-filled numbers in the board are fixed and cannot be altered.
# The usual way of getting to next stage dfs(x+1, y), dfs(x-1, y), ... is bonded to problems that related to
# "adjacent cell xxx"
# But in Sudoku problem, the next stage (cell) of DFS does not have to be an adjacent cell, so use a
# find_next_empty_cell() function.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    seen.add((1, i, board[i][j])) # 1 means this is a row
                    seen.add((2, j, board[i][j])) # 2 means this is a column
                    seen.add((3, i // 3, j // 3, board[i][j])) # 3 means this is a sub-board

        # Find the next empty cell
        def find_next_empty_cell():
            for i in range(9):  # cant do trimming like range(x, 9) -> that's wrong!
                for j in range(9):
                    if board[i][j] == '.':
                        return [i, j]

        def dfs(x: int, y: int, seen) -> bool:
            if x < 0 or x >= 9 or y < 0 or y >= 9:
                return

            tmp = find_next_empty_cell()
            if not tmp:
                return True
            else:
                x, y = tmp[0], tmp[1]

            for c in '123456789':
                if (1, x, c) not in seen and (2, y, c) not in seen and (3, x // 3, y // 3, c) not in seen:
                    board[x][y] = c
                    seen.add((1, x, c))
                    seen.add((2, y, c))
                    seen.add((3, x // 3, y // 3, c))

                    if dfs(x, y, seen):
                        return True  # we are told that there is only one solution. If found no need to continue.

                    board[x][y] = '.'
                    seen.remove((1, x, c))
                    seen.remove((2, y, c))
                    seen.remove((3, x // 3, y // 3, c))

            return False

        dfs(0, 0, seen)
        return

# Backtrack
# T: (9!)^9 for a 9x9 board. For each row, there are 9! combinations. We have 9 rows, so total 9! * 9! * ... = 9!^9 combinations
#   Or, it is O((m*n)^9)
# S: O(1)
# Note that the board is a 2d string array (since it uses "." to represent empty).
#   - This can be changed to to 2d integer array
#   The starting row/col index of the box for a given (row, col) element
#        boxrow = row - row%3
#        boxcol = col - col%3
# class Solution:
#     def solveSudoku(self, board: list[list[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         self.board = board # Give class a member of board
#         self.solve()
#
#     def find_next_unassigned(self):
#         for row in range(9):
#             for col in range(9):
#                 if self.board[row][col] == ".":
#                     return row, col
#         return -1, -1
#
#     def solve(self):
#         row, col = self.find_next_unassigned()
#         # no unassigned position is found, puzzle solved
#         if row == -1 and col == -1:
#             return True
#         for num in "123456789":
#             if self.isSafe(row, col, num):
#                 self.board[row][col] = num
#                 if self.solve():
#                     return True
#                 self.board[row][col] = "."
#         return False
#
#     def isSafe(self, row, col, ch):
#         boxrow = row - row % 3
#         boxcol = col - col % 3
#         if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
#             return True
#         return False
#
#     def checkrow(self, row, ch):
#         for col in range(9):
#             if self.board[row][col] == ch:
#                 return False
#         return True
#
#     def checkcol(self, col, ch):
#         for row in range(9):
#             if self.board[row][col] == ch:
#                 return False
#         return True
#
#     def checksquare(self, row, col, ch):
#         for r in range(row, row + 3):
#             for c in range(col, col + 3):
#                 if self.board[r][c] == ch:
#                     return False
#         return True
