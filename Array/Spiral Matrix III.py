# 885. Spiral Matrix III
# Intuition:
# Take steps one by one.
# If the location is inside of grid, add it to res.
# But how to simulate the path?

# It seems to be annoying, but if we observe the path:

# move right 1 step, turn right
# move down 1 step, turn right
# move left 2 steps, turn right
# move top 2 steps, turn right,
# move right 3 steps, turn right
# move down 3 steps, turn right
# move left 4 steps, turn right
# move top 4 steps, turn right,

# we can find the sequence of steps: 1,1,2,2,3,3,4,4,5,5....

# So there are two thing to figure out:

# how to generate sequence 1,1,2,2,3,3,4,4,5,5
# how to turn right?

# Generate sequence 1,1,2,2,3,3,4,4,5,5
# Let n be index of this sequence.
# Then A0 = 1, A1 = 1, A2 = 2 ......
# We can find that An = n // 2 + 1


# How to turn right?
# Note that the four directions in sequence are {{0,1},{1,0},{0,-1},{-1,0}}
#   So dx, dy, n = dy, -dx
# Or
#   By cross product:
#   Assume current direction is (x, y) in plane, which is (x, y, 0) in space.
#   Then the direction after turn right (x, y, 0) × (0, 0, 1) = (y, -x, 0)
#   Translate to code: tmp = x; x = y; y = -tmp;

# By arrays of arrays:
# The directions order is (0,1),(1,0),(0,-1),(-1,0), then repeat.
# Just define a variable.


# Time Complexity:
# Time O(max(R,C)^2)
# Space O(R*C) for output

class Solution:
    def spiralMatrixIII(self, R, C, x, y):
        res = []
        n = 0  # number of turns so far
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction_index = 0

        while len(res) < R * C:
            dx, dy = directions[direction_index % 4]

            for i in range(n // 2 + 1):
                if 0 <= x < R and 0 <= y < C:
                    res.append([x, y])
                x, y = x + dx, y + dy

            n += 1
            direction_index += 1

        return res