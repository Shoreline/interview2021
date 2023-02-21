# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Note that only node.val is returned, not the whole node
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
# copied and revised
# T: O(nlogn), S: O(n)
import collections


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_values = collections.defaultdict(list)  # a map of <col, [(row1,val1), (row2,val2), ...]>

        def dfs(root: Optional[TreeNode], row: int, col: int):
            if not root:
                return
            col_values[col].append((row, root.val))
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []
        for i in sorted(col_values):  # sorted(col_values) returns a sorted list of keys in col_values
            # sort a list of [(row1,val1), (row2,val2)...]. Sorting compares all first elements, then the 2nd.
            col_values[i].sort()
            res.append([val for row, val in col_values[i]])
        return res

# wrong answer. can't simply sort all values in a vertical, but first sort by row number, then for the same row number sort by value
# import collections
# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         cols = collections.defaultdict(list)
#         queue = [(root, 0)]
#         for node, i in queue:
#             if node:
#                 cols[i].append(node.val)
#                 queue += (node.left, i - 1), (node.right, i + 1)

#         res = []
#         for i in sorted(cols):
#             cols[i].sort()
#             res.append(cols[i])
#         return res        