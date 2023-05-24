# The idea is quite straightforward:
# In each round, pick the smallest number within k distance and move it to the front.
# For each number, we save its indexes in a deque.
# In each round, we check from 0 to 9 to see if the nearest index is within k distance.
# But here comes the tricky part:
# The index of a number may change due to the swaps we made in the previous rounds.
# For example, if 3 numbers after num[i] are moved to the front,
# then the index of num[i] becomes i + 3 in the new array.
# So we need a data structure to store the indexes of picked numbers,
# to support fast calculation of the new index of each remaining number.
# BIT, Segment Tree and Balanced Binary Search Tree can do this.
# Here I use sortedcontainers, which is an implementation of Balanced Binary Search Tree.

from collections import defaultdict, deque
from sortedcontainers import SortedList
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        d = defaultdict(deque) # map<digit, deque<index>>
        for i, a in enumerate(num):
            d[a].append(i)
        ans, seen = '', SortedList()
        for _ in range(len(num)):
            for a in '0123456789':  # check from small digit to big digit
                if d[a]:    # if this digit exist
                    i = d[a][0]
                    new_i = i + len(seen) - seen.bisect(i) # len(seen): how many times we have moved a digit forward
                    dis = new_i - len(seen)
                    if dis <= k:
                        k -= dis
                        d[a].popleft()
                        ans += a
                        seen.add(i)
                        break   # each time, only move the current smallest digit
        return ans