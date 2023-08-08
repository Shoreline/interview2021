# Similar to best meeting point, but 1) this problem has obstacles; 2) can only build (meet) on empty land
# BFS, use queue
# T: O(M^2 * N^2) Do m*n times of BFS, each takes m*n
# S: O(M * N)
# Compute the shortest total dist of each empty land to ALL buildings (sum(min_dist(a_land, house)))
#   use another 2d array dist_sum to save the sum of shortest distance for each empty land to all buildings.
#   house is one of the houses.
# From houses to reach empty land -> faster when there are fewer houses than land

from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # dist_sum[i,j]: the total distance from this land to all buildings
        # dist_sum only has valid value for empty lands
        dist_sum = [[0] * cols for _ in range(rows)]

        # Instead of using a visited_set, simply modify the value representing empty_land for each complete BFS-loop
        # (one BFS-loop per house, it has many rounds of BFS iterations).
        #
        # The value that represents an empty land. Will decrement once done traversing a house
        # The reason to change value representing empty land is to differentiate rounds of BFS
        # Initial value is defined by the problem statement (which is 0)
        empty_land = 0  # will go from 0, to -1, -2, -3, ... no need to reset

        for i in range(rows):
            for j in range(cols):
                # Only proceed for tile of house
                # So if there are a lot less house tiles than empty tiles, we can save computation
                if grid[i][j] != 1:
                    continue

                q = deque([[i, j]])  # same as q = deque() and q.append([i,j])
                steps = 0
                while q:
                    steps += 1
                    cur_queue_length = len(q)
                    for k in range(cur_queue_length):
                        x, y = q.popleft()
                        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == empty_land:
                                # mark it with the next round's empty_land value
                                grid[x + dx][y + dy] = empty_land - 1
                                dist_sum[x + dx][y + dy] += steps
                                q.append([x + dx, y + dy])

                empty_land -= 1  # same indent with "while q:"

        min_dist = float('inf')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == empty_land:
                    min_dist = min(min_dist, dist_sum[i][j])

        return min_dist if min_dist < float('inf') else -1