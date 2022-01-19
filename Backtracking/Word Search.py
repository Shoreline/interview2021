# T: O(board_size * 3^word_length): 3 directions to search (the one going back will get rejected immediately)
# S: O(word_length) recursion depth
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # problem statement says that the board is not empty
        def helper(i: int, j: int, pos: int) -> bool:
            if pos == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] == word[pos]:
                tmp, board[i][j] = board[i][j], '.'
                if (helper(i + 1, j, pos + 1) or helper(i - 1, j, pos + 1) or helper(i, j + 1, pos + 1) or helper(i,
                                                                                                                  j - 1,
                                                                                                                  pos + 1)):
                    return True
                board[i][j] = tmp

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):
                    return True
        return False