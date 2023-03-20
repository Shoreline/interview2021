# T: O(m * n)
# S: O(1)

# Note that we only need to evaluate the very next stage!
#   No need to repeatedly run.
#
# cur round live: abs(cell) == 1
#   cur round live and next round live: 1 # unchanged
#   cur round live and next round dead: -1
#
# cur round dead: abs(cell) != 1
#   cur round dead and next round live: 2
#   cur round dead and next round dead: 0 # unchanged
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        def countLiveNeighbors(i: int, j: int) -> int:
            res = 0
            for n in neighbors:
                r = i + n[0]
                c = j + n[1]
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if abs(board[r][c]) == 1:
                        res += 1

            return res

        # deal with the cases where there is a state change
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = countLiveNeighbors(i, j)
                if board[i][j] == 1 and live_neighbors not in (2,3):  # live -> dead
                    board[i][j] = -1 # so abs(board[i][j]) is still 1
                if board[i][j] == 0 and live_neighbors == 3:  # dead -> live
                    board[i][j] = 2 # temporally mark it as 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in (1, 2):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return
    # A more general solution Keep update cur value, but make a cur_to_pre function, so we are able to know the pre
    # status of a cell as well. To save space, use a map to save states transitions (new_turn_val -> old_turn_val).
    # There are only 4 of such transitions. We can then flip cells in-place while still being able to know the
    # previous value for flipped cells
    def gameOfLife2(self, board: List[List[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # now -> pre: 2->0 ; 3->1
        trans_map = {2: 0, 3: 1}

        def countLiveNeighbors(i: int, j: int, neighbors: List[List[int]]) -> int:
            res = 0
            for n in neighbors:
                r = i + n[0]
                c = j + n[1]
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    val = trans_map[board[r][c]] if board[r][c] in trans_map else board[r][c]
                    if val == 1:
                        res += 1

            return res

        # deal with the cases where there is a state change
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = countLiveNeighbors(i, j, neighbors)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):  # live -> dead
                    board[i][j] = 3
                if board[i][j] == 0 and live_neighbors == 3:  # dead -> live
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in (1, 2):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return

