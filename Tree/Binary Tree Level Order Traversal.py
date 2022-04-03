# Do level traverse, maintains a map of <col_val, [list node_val]>

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = collections.defaultdict(list)
        q = deque([(root, 0)])  # queue saves a tuple of (node, column_value)
        while q:  # Column_value is enough to tell vertical order, no need to have delimiter
            node, col_val = q.popleft()
            cols[col_val].append(node.val)

            if node.left:
                q.append((node.left, col_val - 1))
            if node.right:
                q.append((node.right, col_val + 1))

        return [cols[i] for i in sorted(cols)]

    # class Solution:
#     def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         cols = collections.defaultdict(list)
#         queue = [(root, 0)] # queue saves a tuple of (node, column_value)
#         for node, i in queue: # Column_value is enough to tell vertical order, no need to have delimiter
#             if node:
#                 cols[i].append(node.val)
#                 queue += (node.left, i - 1), (node.right, i + 1)
#         return [cols[i] for i in sorted(cols)]
