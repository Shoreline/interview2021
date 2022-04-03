# Do level traverse, maintains a map of <col_val, [list node_val]>

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = collections.defaultdict(list)
        queue = [(root, 0)]  # queue saves a tuple of (node, column_value)
        for node, i in queue:  # Column_value is enough to tell vertical order, no need to have delimiter
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
