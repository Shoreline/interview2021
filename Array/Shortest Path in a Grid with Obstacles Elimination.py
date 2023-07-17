# 0 is empty; 1 is obstacle

# A star algo
# O(N⋅K⋅log(N⋅K)): Let N be the number of cells in the grid, and K be the quota to eliminate obstacles.
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        target = (m - 1, n - 1)

        # Returns the distance between in put coordinates and the target coordinate
        def get_dist(x, y):
            return target[0] - x + target[1] - y

        # (x, y, removed_obs)
        state = (0, 0, 0)

        # (min_path_length, steps, state)
        # note, must use min_path_length, not min_remaining_path_length to sort item in heap. Otherwise wrong.
        # h(n) = manhattan distance,  g(n) = 0
        queue = [(get_dist(0, 0), 0, state)]
        seen = set([state])

        while queue:
            # prioritize trying the tile with the shortest possible path length
            min_dist, steps, state = heapq.heappop(queue)
            x, y, removed_obs = state

            # If we can reach the target in the shortest path (manhattan distance),
            #   even if all remaining path are obstacle -> found the shortest path.
            if min_dist - steps <= (k - removed_obs):
                return min_dist

            # explore the four directions in the next step
            for i, j in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                # if (new_row, new_col) is within the grid boundaries
                if 0 <= i < m and 0 <= j < n:
                    new_removed_obs = removed_obs  # can't just modify removed_obs -> it is part of a tuple (state)
                    if grid[i][j] == 1:
                        new_removed_obs += 1
                        # removed_obs += 1
                    new_state = (i, j, new_removed_obs)

                    # if the next direction is worth exploring
                    if new_removed_obs <= k and new_state not in seen:
                        seen.add(new_state)
                        # new_min_dist = get_dist(i, j) + steps + 1
                        heapq.heappush(queue, (get_dist(i, j) + steps + 1, steps + 1, new_state))

        # did not reach the target
        return -1


# BFS
# But with a different node definition: [x, y, obstacles_removed]
# T: O(n*k) # n: num of cells in grid
class Solution_bfs:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Node definition:[x, y, obstacles_removed]
        # To be used in the queue and visited set.
        q = collections.deque([(0, 0, 0)])
        visited = set()

        m, n = len(grid), len(grid[0])
        dist = 0

        while q:
            size = len(q)
            for _ in range(size):
                x, y, removed_obs = q.popleft()

                # wrong: there can be another shorter path
                # remaining_d = abs(x - (m -1)) + abs(y - (n - 1))
                # if k - obstacle >= remaining_d:
                #     return dist + remaining_d
                if x == m - 1 and y == n - 1:
                    return dist

                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= i < m and 0 <= j < n:
                        # if next tile is an obstacle, but we can remove it
                        if grid[i][j] == 1 and removed_obs < k and (i, j, removed_obs + 1) not in visited:
                            visited.add((i, j, removed_obs + 1))
                            q.append((i, j, removed_obs + 1))

                        # if next tile is empty
                        if grid[i][j] == 0 and (i, j, removed_obs) not in visited:
                            visited.add((i, j, removed_obs))
                            q.append((i, j, removed_obs))

            dist += 1

        return -1
