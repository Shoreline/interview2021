class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n, = len(maze), len(maze[0])
        stopped = set()

        def dfs(x, y):
            if (x, y) in stopped:
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x, y
                # Keep rolling in this direction, until hitting a wall
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] != 1:
                    new_x += dx
                    new_y += dy
                if dfs(new_x, new_y):
                    return True
            return False

        return dfs(start[0], start[1])
