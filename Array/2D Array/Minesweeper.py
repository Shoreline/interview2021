# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        d = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])

        def dfs(B, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            if B[i][j] == 'M':
                B[i][j] = 'X'  # hit a mine -> GG
            elif B[i][j] == 'E':  # count adjacent mines
                mines = 0
                for x, y in d:
                    if 0 <= i + x < m and 0 <= j + y < n and B[i + x][j + y] == 'M':
                        mines += 1

                B[i][j] = str(mines) if mines > 0 else 'B'

                if mines == 0:  # only extend for a blank cell
                    for x, y in d:
                        dfs(B, i + x, j + y)
            return B

        return dfs(board, click[0], click[1])