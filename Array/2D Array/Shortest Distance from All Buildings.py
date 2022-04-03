# Similar to best meeting point, but 1) this problem has obstackles; 2) can only build (meet) on empty land
# BFS, use queue
# Compute the shortest total dist of each land to ALL buildings (sum(min_dist(a_land, house))) | house is one of the house.
# From houses to reach empty land -> faster when there are less houses than land

from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])

        # dist_sum[i,j]: the total distance from this land to all buildings
        # dist_sum only has valid value for empty lands
        dist_sum = [[0] * cols for _ in range(rows)]

        # The value that represents an empty land. Will decrement once done traversing a house
        # The reason to change value representing empty land is to differenciate rounds of BFS
        # Initial value is defined by the problem statement (which is 0)
        empty_land = 0  # will go from 0, to -1, -2, -3, ...

        for i in range(rows):
            for j in range(cols):
                # Only proceed for tile of house
                # So if there are a lot less house tiles than empty tiles, we can save computation
                if grid[i][j] != 1:
                    continue

                q = deque([[i, j]])  # same as q = deque() and q.append([i,j])
                steps = 0
                # Keep resetting the min_dist for every house.
                # So only the last house will output meaningful min_dist
                min_dist = float('inf')

                while q:
                    steps += 1
                    cur_queue_length = len(q)
                    for k in range(cur_queue_length):
                        cur_cell = q.popleft()
                        for direction in directions:
                            next_cell = [cur_cell[0] + direction[0], cur_cell[1] + direction[1]]
                            if next_cell[0] >= 0 and next_cell[0] < rows and next_cell[1] >= 0 and next_cell[
                                1] < cols and grid[next_cell[0]][next_cell[1]] == empty_land:
                                # mark it with the next round's empty_land value
                                grid[next_cell[0]][next_cell[1]] = empty_land - 1
                                dist_sum[next_cell[0]][next_cell[1]] += steps

                                q.append(next_cell)

                empty_land -= 1  # same indent with "while q:"

        min_dist = float('inf')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == empty_land:
                    min_dist = min(min_dist, dist_sum[i][j])

        return min_dist if min_dist < float('inf') else -1

# from collections import deque
# class Solution:
#     def shortestDistance(self, grid: List[List[int]]) -> int:
#         directions =[[1,0], [-1,0], [0,1], [0, -1]]
#         rows = len(grid)
#         cols = len(grid[0])

#         # dist_sum[i,j]: the total distance from this land to all buildings
#         # dist_sum only has valid value for empty lands
#         dist_sum = [[0]*cols for _ in range(rows)]
#         min_dist = float('inf')

#         # The value that represents an empty land. Will decrement once done traversing a house
#         # Initial value is defined by the problem statement (which is 0)
#         empty_land = 0


#         for i in range(rows):
#             for j in range(cols):
#                 # Only proceed for tile of house
#                 # So if there are a lot less house tiles than empty tiles, we can save computation
#                 if grid[i][j] != 1:
#                     continue

#                 q = deque()
#                 q.append([i, j])
#                 steps = 0
#                 # Keep resetting the min_dist for every house.
#                 # So only the last house will output meaningful min_dist
#                 min_dist = float('inf')

#                 while q:
#                     steps += 1
#                     cur_queue_length = len(q)
#                     for k in range(cur_queue_length):
#                         cur_cell = q.popleft()
#                         for direction in directions:
#                             next_cell = [cur_cell[0] + direction[0], cur_cell[1] + direction[1]]
#                             if next_cell[0] >=0 and next_cell[0] < rows and next_cell[1]>=0 and next_cell[1]<cols and grid[next_cell[0]][next_cell[1]] == empty_land:
#                                 # mark it with the next round's empty_land value
#                                 grid[next_cell[0]][next_cell[1]] = empty_land - 1
#                                 dist_sum[next_cell[0]][next_cell[1]] += steps
#                                 min_dist = min(min_dist, dist_sum[next_cell[0]][next_cell[1]])

#                                 q.append(next_cell)

#                 empty_land -= 1 # same indent with "while q:"

#         return min_dist if min_dist < float('inf') else -1
