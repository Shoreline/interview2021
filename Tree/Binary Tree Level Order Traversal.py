# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

        return res
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#
#         res = []
#         cur_lvl = [root]
#         next_lvl = []
#         while cur_lvl:
#             tmp = []
#             for node in cur_lvl:
#                 tmp.append(node.val)
#                 if node.left:
#                     next_lvl.append(node.left)
#                 if node.right:
#                     next_lvl.append(node.right)
#             res.append(tmp[:])
#             cur_lvl = next_lvl
#             next_lvl = []
#
#         return res

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#
#         res = []
#         cur_lvl = [root]
#         next_lvl = []
#         while cur_lvl:
#             tmp = []
#             for node in cur_lvl:
#                 if node:
#                     tmp.append(node.val)
#                     next_lvl.append(node.left)
#                     next_lvl.append(node.right)
#             if tmp:  # easy to mistakenly insert empty tmp list
#                 res.append(tmp[:])
#             cur_lvl = next_lvl
#             next_lvl = []
#
#         return res

    # class Solution:
#     def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         cols = collections.defaultdict(list)
#         queue = [(root, 0)] # queue saves a tuple of (node, column_value)
#         for node, i in queue: # Column_value is enough to tell vertical order, no need to have delimiter
#             if node:
#                 cols[i].append(node.val)
#                 queue += (node.left, i - 1), (node.right, i + 1)
#         return [cols[i] for i in sorted(cols)]
