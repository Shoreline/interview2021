# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Use queue
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])
        order = True
        while q:
            cur_lvl_len = len(q)
            next_lvl = []
            for i in range(cur_lvl_len):
                node = q.popleft()
                next_lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if order:
                res.append(next_lvl)
            else:
                res.append(next_lvl[::-1])
            order = not order

        return res

# Use two stacks
# O(n) / O(n)
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         res = []
#         cur_lvl = [root]
#         next_lvl = []

#         left_first = True
#         while cur_lvl:
#             lvl_res = []
#             while cur_lvl:
#                 node = cur_lvl.pop()
#                 if not node:
#                     continue
#                 lvl_res.append(node.val)

#                 if left_first:
#                     next_lvl.append(node.left)
#                     next_lvl.append(node.right)
#                 else:
#                     next_lvl.append(node.right)
#                     next_lvl.append(node.left)
#             cur_lvl = next_lvl
#             next_lvl = [] # Can't use next_lvl.clear(), otherwise cur_lvl gets cleared as well
#             if lvl_res:
#                 res.append(lvl_res)
#             left_first = not left_first

#         return res    