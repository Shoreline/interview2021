# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False


# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#
#         def double_inorder(root1, root2):
#             if not root1 and not root2:
#                 return True
#             elif root1 and root2:
#                 left = double_inorder(root1.left, root2.left)
#                 if not left:
#                     return False
#                 if root1.val != root2.val:
#                     return False
#                 return double_inorder(root1.right, root2.right)
#             else:
#                 return False
#
#         return double_inorder(p, q)