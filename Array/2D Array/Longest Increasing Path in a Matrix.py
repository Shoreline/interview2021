# DFS with memorization (top-down DP)
# TLE if use @lru_cache() (limit size to 128), but @lru_cache(None) works
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        @lru_cache(None)  # TLE if use @lru_cache(). None means no maxsize for the cache.
        def dfs(i, j) -> int:
            res = 1  # at least count this cell itself
            for d in dirs:
                r, c = i + d[0], j + d[1]
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] > matrix[i][j]:
                    res = max(res, 1 + dfs(r, c))

            return res

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))

        return res

# Self defined cache instead of lru_cache@
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         DIRS = [[1,0], [-1,0], [0, 1], [0, -1]]
#         cache = [[0] * len(matrix[0]) for _ in range(len(matrix))]

#         def dfs(i, j) -> int:
#             if cache[i][j] > 0:
#                 return cache[i][j]

#             res = 1 # at least count this cell itself
#             for d in DIRS:
#                 r, c = i + d[0], j + d[1]
#                 if 0<= r < len(matrix) and 0<= c < len(matrix[0]) and matrix[r][c] > matrix[i][j]:
#                     res = max(res , 1 + dfs(r,c))

#             cache[i][j] = res # don't forget to save result in the cache
#             return res


#         res = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 res = max(res, dfs(i,j))

#         return res


# Can also be solved by topological sort
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/1429348/C%2B%2BPython-2-solutions%3A-DFS-and-Memoization-Topology-Sort-Peel-Onion-Clean-and-Concise        