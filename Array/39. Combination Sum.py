# Backtracking
# O(N ^ (T / M + 1)) : Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
# T/M: the largest combination size (length of the combination with the most elements)
# As we illustrated before, the execution of the backtracking is unfolded as a DFS traversal in a n-ary tree. The total number of steps during the backtracking would be the number of nodes in the tree.
# A N-ary tree is a rooted tree in which each node has no more than n children.
# The maximal depth of the tree is T / M.
# The maximal number of a N-ary tree with T/M depth is N ^ (T/M + 1)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(remaining: int, pos: int, tmp: List[int]):
            if remaining == 0:
                res.append(list(tmp))
            elif remaining < 0:
                return

            for i in range(pos, len(candidates)):
                tmp.append(candidates[i])
                dfs(remaining - candidates[i], i, tmp)
                tmp.pop()

        dfs(target, 0, [])
        return res

# faster?
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         self.dfs(candidates, target, 0, [], res)
#         return res

#     def dfs(self, candidates: List[int], target: int, pos: int, tmp: List[int], res: List[List[int]]):
#         if (target == 0):
#             res.append(list(tmp))
#             #res.append(tmp[:]) # also works
#             return
#         elif target < 0:
#             return

#         for i in range(pos, len(candidates)):
#             if(candidates[i] > target):
#                 break
#             tmp.append(candidates[i])
#             self.dfs(candidates, target - candidates[i], i, tmp, res)
#             tmp.pop()

# import copy
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         self.dfs(candidates, target, 0, [], res)
#         return res

#     def dfs(self, candidates: List[int], target: int, pos: int, tmp: List[int], res: List[List[int]]):
#         if (target == 0):
#             res.append(copy.deepcopy(tmp))
#             return
#         elif pos >= len(candidates) or target < 0:
#             return

#         for i in range(pos, len(candidates)):
#             if(candidates[i] > target):
#                 break
#             tmp.append(candidates[i])
#             self.dfs(candidates, target - candidates[i], i, tmp, res)
#             tmp.pop()

