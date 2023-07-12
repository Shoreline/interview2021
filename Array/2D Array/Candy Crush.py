# Time: O(M*N)
# Space: O(1)
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            # 1, Check
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if i >= 2 and board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        # crush = crush.union({(i, j), (i - 1, j), (i - 2, j)}) # same
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}

                    if j >= 2 and board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}

            # 2, Crush
            if not crush:
                break
            for i, j in crush:
                board[i][j] = 0

            # 3, Drop
            for j in range(len(board[0])):  # process one column by one column
                bottom = len(board) - 1  # Points to the bottom row where candies can be dropped on

                # everytime there is a candy, move it to the bottom row, then raise the bottom row
                for i in range(len(board) - 1, -1, -1):
                    if board[i][j]:
                        board[bottom][j] = board[i][j]
                        if bottom != i:
                            board[i][j] = 0
                        bottom -= 1
        return board
