# The idea is quite straightforward:
# In each round, pick the smallest number within k distance and move it to the front.
#   so each round can cost >1 moves
# For each number, we save its indexes in a deque.
# In each round, we check from 0 to 9 to see if the nearest index is within k distance.
# But here comes the tricky part:
# The index of a number may change due to the swaps we made in the previous rounds.
# For example, if 3 numbers after num[i] have been moved to the front,
# then the index of num[i] becomes i + 3 in the new array.

# So we need a data structure to store the indexes of picked numbers,

# bisect.bisect_right(): some digits may be placed ahead of current_digit in the initial input
# So do bisect_right to avoid over counting of swaps.

# to support fast calculation of the new index of each remaining number.
# BIT, Segment Tree and Balanced Binary Search Tree can do this.
# Here I use sortedcontainers, which is an implementation of Balanced Binary Search Tree.
import bisect
from collections import defaultdict, deque


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        d = defaultdict(deque)  # map<digit, deque<index>>
        for i, a in enumerate(num):
            d[a].append(i)

        # moved: a sorted list of moved digits
        ans, moved = '', []
        for _ in range(len(num)):
            for a in '0123456789':  # check from small digit to big digit
                if d[a]:  # if this digit exist
                    i = d[a][0]
                    # bisect.bisect_right(moved, i) : the new index of this index
                    # bisect.bisect_right(): some digits may be placed ahead of current_digit in the initial input
                    # So do bisect_right to avoid over counting of swaps.
                    dis = i - bisect.bisect_right(moved, i)
                    # at some point k == 0
                    if dis <= k:
                        k -= dis
                        ans += a
                        bisect.insort_right(moved, d[a].popleft())
                        break  # each time, only move the current smallest digit
        return ans