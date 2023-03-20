# 1) No obstacle!
# 2) ok to meet at a both '0' and '1' tile.
# Usually use BFS for this sort of problems: T O((mn)^2); S: O(mn)
#   (or O(N^2) and O(N), where N is the total number of elements in the grid)
# But there are faster ways for this problem:
# Math: the optimal meeting point is any point that separates two equal number of points
#   For points like this, if it is closer to group 1 means it is farther from group 2
#   -> The problem becomes finding the median of x and y coordinates
#       1) We can use sort(), but there is some more efficient way: finding the k-th smallest element (O(mn))
#       2) Pick any two points from the two groups, the total distance of say x_axis is always p2_x - p1_x
#           No matter where you set a 3rd meeting point, where total distance is (p2_x - p3_x) + (p3_x - p1_x)
#           So no need to really find that meeting point! O(mn)

# Best O(mn) and O(mn) solution
# No need to actually find the meeting point, we can compute minimal distance.
# To actually find the meeting point we have to do below sorting solution.
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # find the median of x and y indices
        x_indices = []
        y_indices = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x_indices.append(i)
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    y_indices.append(j)

        if len(x_indices) == 0:
            return 0

        x_median = x_indices[len(x_indices) // 2]
        y_median = y_indices[len(y_indices) // 2]
        res = 0
        for x in x_indices:
            res += abs(x - x_median)
        for y in y_indices:
            res += abs(y - y_median)

        return res

# class Solution:
#     def minTotalDistance(self, grid: List[List[int]]) -> int:
#         rows, cols = [], []
#         # To ensure rows and cols are sorted:
#         #   Must iterate the board twice, once prioritize rows, once prioritize cols
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     rows.append(i)
#         for j in range(len(grid[0])):
#             for i in range(len(grid)):
#                 if grid[i][j] == 1:
#                     cols.append(j)
#
#         res = 0
#         # Compute the total distance directly, no need to find the median!
#         i, j = 0, len(rows) - 1  # obviously, rows and cols have the same length
#         while i < j:
#             res += rows[j] - rows[i]
#             res += cols[j] - cols[i]
#             i += 1
#             j -= 1
#
#         return res

# Sorting solution: T O(mnlog(mn)); S O(mn) (there can be at most m*n points)
# This solution does find the best meeting point.
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
