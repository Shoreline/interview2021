# BFS
# Count number of fresh oranges first;
# BFS for every rotten orange, see after how many rounds the #fresh oranges is 0.
# T: O(m*n), S: O(m*n)
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()  # saves rotten cells
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        round = 0

        # Note, we can only increment round, when at least one fresh orange turns into rotten.
        # Corner case: all oranges are already rotten at the beginning -> returns 0
        while queue:
            new_rotten = 0
            size = len(queue)
            for i in range(size):
                cell = queue.popleft()
                for dir in dirs:
                    r, c = cell[0] + dir[0], cell[1] + dir[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        new_rotten += 1
            round = round + 1 if new_rotten > 0 else round
            fresh_oranges -= new_rotten

        return round if fresh_oranges == 0 else -1
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         queue = deque()  # The queue tracking rotten cells
#         fresh_oranges = 0
#         # Add all initial rotten cells to the queue as queue's starting status
#         # They will start to infect neighboring oranges at the same time.
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 2:
#                     queue.append((i, j))
#                 elif grid[i][j] == 1:
#                     fresh_oranges += 1
#         queue.append((-1, -1))  # use (-1,-1) as a separator between two rounds
#
#         time = 0
#         directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#         while queue:
#             x, y = queue.popleft()
#             if x == -1:  # End of a round
#                 if not queue:
#                     break
#                 else:
#                     time += 1  # need more time to process the next round
#                     queue.append((-1, -1))
#             else:
#                 for d in directions:
#                     x2, y2 = x + d[0], y + d[1]
#                     if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 1:
#                         grid[x2][y2] = 2  # label this cell as rotten
#                         fresh_oranges -= 1  # decrement number of fresh oranges after flipping
#                         queue.append((x2, y2))
#
#         return time if fresh_oranges == 0 else -1

# for each island, scan twice.
# 1) find and save locations of rotten oranges in this island;
# 2) for each fresh orage in the island, iteration the set of rotten oranges to find the cloest one. Time needs to get rotten is x1-x2 + (y1-y2)
# -> Time O(m*n + m*n*(m*n)), space O(1)