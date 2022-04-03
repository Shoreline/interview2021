# 1) No obstackle!
# 2) ok to meet at a both '0' and '1' tile.
# BFS is too slow: T O((mn)^2); S: O(mn)
# Math: the optimal meeting point is any point that separates two equal number of points
#   For points like this, if it is closer to group 1 means it is farther from group 2
#   -> The problem becomes finding the median of x and y coordinates
#       1) We can use sort(), but there is some more efficient way: finding the k-th smallest element (O(mn))
#       2) Pick any two points from the two groups, the total distance is always p2 - p1.
#          So no need to really find the median! O(mn)

# Best O(mn) and O(mn) solution
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = [], []
        # To ensure rows and cols are sorted:
        #   Must iterate the board twice, once prioritize rows, once prioritize cols
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    cols.append(j)

        res = 0
        # Compute the total distance directly, no need to find the median!
        i, j = 0, len(rows) - 1  # obviously, rows and cols have the same length
        while i < j:
            res += rows[j] - rows[i]
            res += cols[j] - cols[i]
            i += 1
            j -= 1

        return res

# Sorting solution: T O(mnlog(mn)); S O(mn) (there can be at most m*n points)
# class Solution(object):
#     def minTotalDistance(self, grid: List[List[int]]) -> int:
#         M,N = len(grid),len(grid[0])
#         rows, cols = [], []
#         for i in range(M):
#             for j in range(N):
#                 if grid[i][j] == 1:
#                     rows.append(i)
#                     cols.append(j)

#         rows.sort()
#         cols.sort()

#         meet_point = (rows[len(rows)//2], cols[len(cols)//2])

#         res = 0
#         for x in rows:
#             res += abs(meet_point[0] - x)
#         for y in cols:
#             res += abs(meet_point[1] - y)
#         return res
