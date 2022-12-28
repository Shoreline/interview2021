# T: O(board_size * 3^word_length): 3 directions to search (the one going back will get rejected immediately)
# S: O(word_length) recursion depth
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # problem statement says that the board is not empty
        # @lru_cache(None) wrong if use lru_cache!
        def bt(pos, x, y):
            if pos == len(word):
                return True            

            if 0<=x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[pos]:
                board[x][y] = '.'
                for i, j in [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]:
                    if bt(pos + 1, i, j):
                        return True
                board[x][y] = word[pos]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt(0, i, j):
                    return True
        return False

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         # problem statement says that the board is not empty
#         def helper(i: int, j: int, pos: int) -> bool:
#             if pos == len(word):
#                 return True
#             if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
#                 return False
#             if board[i][j] == word[pos]:
#                 tmp, board[i][j] = board[i][j], '.'
#                 if (helper(i + 1, j, pos + 1) or helper(i - 1, j, pos + 1) or helper(i, j + 1, pos + 1) or helper(i,
#                                                                                                                   j - 1,
#                                                                                                                   pos + 1)):
#                     return True
#                 board[i][j] = tmp

#             return False

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if helper(i, j, 0):
#                     return True
#         return False
