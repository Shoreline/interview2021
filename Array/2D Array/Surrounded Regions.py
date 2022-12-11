# /*
#  * Flood fill
#  *
#  * Idea: do not look for surrounded regions directly. Flood fill all 'O'
#  * regions that connected to an edge with the third color. Except these regions,
#  * all other 'O' regions shall be flipped to 'X'
#  *
#  * Important: Different between queue.add() and queue.offer() in Java; When to
#  * flag node while doing BFS
#  */
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def flood_flip(i: int, j: int, target: str, replacement: str) -> None:
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == target:
                for d in directions:
                    board[i][j] = replacement
                    flood_flip(i + d[0], j + d[1], target, replacement)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == "O":
                    flood_flip(i, j, 'O', '*')

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return