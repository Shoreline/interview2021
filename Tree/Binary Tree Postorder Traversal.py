# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Do reverse post-order traversal (root -> right -> left), then reverse the result
# Note that reversed post-order is not pre-order!
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            if not cur:
                cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            cur = cur.right

        return reversed(res)
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = [root]
#
#         while stack:
#             root = stack.pop()
#             if root:
#                 res.append(root.val)
#                 stack.append(root.left)
#                 stack.append(root.right)
#
#         return reversed(res)
