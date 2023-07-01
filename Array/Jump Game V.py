# You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.
import functools


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        # number of indice you can jump from i.
        @functools.lru_cache(None)
        def jump(i):
            res = 0
            for direction in [-1, 1]:
                for x in range(1, d + 1):
                    j = i + x * direction
                    # for arr[i], can only jump to places arr[j] that is lower than arr[i], plus there is
                    # no higher arr[k] between i and j.
                    if 0 <= j < len(arr) and arr[j] < arr[i]:
                        res = max(res, jump(j))
                    else:
                        break
            return res + 1

        # return max(jump(index) for index in range(len(arr)))
        res = 0
        for i in range(len(arr)):
            res = max(res, jump(i))
        return res

# The general approach is to construct a DAG from possible jumps downward, then find
# the longest path using DFS. This gives time complexity O(nd).
#   -> topological sort?
#
# To achieve O(n) time
# complexity, we instead consider possible jumps upward, and note the nearest higher
# positions are sufficient. These can be found efficiently using monotone stacks.
# class Solution:
#     def maxJumps(self, A, d):
#         N = len(A)
#         graph = collections.defaultdict(list)

#         def jump(iterator):
#             stack = []
#             for i in iterator:
#                 while stack and A[stack[-1]] < A[i]:
#                     j = stack.pop()
#                     if abs(i - j) <= d:
#                         graph[j].append(i)
#                 stack.append(i)

#         jump(range(N))
#         jump(reversed(range(N)))

#         @lru_cache(maxsize=None)
#         def height(i):
#             return 1 + max(map(height, graph[i]), default=0)

#         return max(map(height, range(N)))