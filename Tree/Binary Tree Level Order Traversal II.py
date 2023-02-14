# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS solution
# (or, simply do regular level order traverse, then reverse the res[])
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        def helper(cur_lvl: list[TreeNode]):
            if not cur_lvl:
                return

            next_lvl = []
            cur_lvl_vals = []
            for node in cur_lvl:
                cur_lvl_vals.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)

            helper(next_lvl)
            res.append(cur_lvl_vals)

        helper([root])
        return res

# class Solution:
#     def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#
#         res = []
#         queue = deque([root])
#         while queue:
#             tmp = []
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 tmp.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(tmp)
#
#         return reversed(res)