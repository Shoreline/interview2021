# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# PS: the initial direction of the robot will be facing up

# backtrack

class Solution:
    def cleanRoom(self, robot):
        # x, y: the relative coordinates based on robot's initial position
        #       NOT the absolute coordinates in the 2D room array
        def dfs(x, y, dx, dy):
            robot.clean()
            visited.add((x, y))

            for i in range(4):
                if (x + dx, y + dy) not in visited and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnLeft()
                dx, dy = -dy, dx

        visited = set()
        return dfs(0, 0, 1, 0)  # can start with any direction

# backtrack
# both T and S: o(n - m) n,m is the number of cells and obstacles
class Solution2:
    def cleanRoom(self, robot):
        visited = set()

        # x, y: relative position for the current position of the robot
        # dx, dy is the previous direction, also passed in.
        def dfs(x, y, dx, dy):
            # 1, Clean current
            robot.clean()
            visited.add((x, y))

            # 2, DFS to the 4 adjacent directions
            # Rotate left 4 times, next tile is the one in front of the robot after turnning left
            # .move() can only move forward
            for _ in range(4):
                # if the next position is not visited and reachable
                if (x + dx, y + dy) not in visited and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                # Note that dfs() will make sure the robot has returned to the original tile and direction
                robot.turnLeft()
                dx, dy = -dy, dx

            # 3, Back to previous position and direction (regardless of current direction)
            # 2 left turns + one move -> turn 180 degree and move one step -> go back one step
            # 2 more left turns -> turn another 180 degree to go back to the original direction
            robot.turnLeft();
            robot.turnLeft()
            robot.move()
            robot.turnLeft();
            robot.turnLeft()

        dfs(0, 0, 0, -1)